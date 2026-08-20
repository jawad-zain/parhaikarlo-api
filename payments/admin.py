from django.contrib import admin
from django.db.models import Case, IntegerField, When
from django.utils import timezone
from django.utils.html import format_html
from datetime import timedelta

from .models import Payment, PaymentMethodOption, Subscription, SubscriptionPlan


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "exam",
        "duration_days",
        "price",
        "is_active",
        "created_at",
    ]
    list_filter = ["exam", "is_active"]
    search_fields = ["name", "exam__name"]
    ordering = ["exam", "price"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "plan",
        "status",
        "starts_at",
        "expires_at",
        "created_at",
    ]
    list_filter = ["status", "plan__exam"]
    search_fields = [
        "user__email",
        "user__username",
        "plan__name",
    ]
    ordering = ["-created_at"]


@admin.action(description="✓ Approve selected (activates their subscription)")
def approve_payments(modeladmin, request, queryset):
    now = timezone.now()
    approved = 0
    skipped = 0

    for payment in queryset.select_related("subscription__plan"):
        if payment.status != "pending":
            skipped += 1
            continue

        subscription = payment.subscription
        plan = subscription.plan

        subscription.status = "active"
        subscription.starts_at = now
        subscription.expires_at = now + timedelta(
            days=plan.duration_days
        )
        subscription.save(
            update_fields=[
                "status",
                "starts_at",
                "expires_at",
                "updated_at",
            ]
        )

        payment.status = "approved"
        payment.save(update_fields=["status", "updated_at"])
        approved += 1

    msg = f"Approved {approved} payment(s) — access is live."
    if skipped:
        msg += f" Skipped {skipped} that weren't pending."
    modeladmin.message_user(request, msg)


@admin.action(description="✗ Reject selected")
def reject_payments(modeladmin, request, queryset):
    rejected = 0
    skipped = 0

    for payment in queryset.select_related("subscription"):
        if payment.status != "pending":
            skipped += 1
            continue

        payment.status = "rejected"
        payment.save(update_fields=["status", "updated_at"])

        # The subscription row was created just for this attempt (a fresh
        # one per submission — see PaymentCreateView) — cancel it too so it
        # doesn't linger as a phantom "pending" sub for the student.
        subscription = payment.subscription
        if subscription.status == "pending":
            subscription.status = "cancelled"
            subscription.save(update_fields=["status", "updated_at"])

        rejected += 1

    msg = f"Rejected {rejected} payment(s)."
    if skipped:
        msg += f" Skipped {skipped} that weren't pending."
    modeladmin.message_user(request, msg)


@admin.register(PaymentMethodOption)
class PaymentMethodOptionAdmin(admin.ModelAdmin):
    list_display = ["label", "method", "instructions", "is_active", "order"]
    list_filter = ["is_active"]
    list_editable = ["order", "is_active"]
    ordering = ["order", "method"]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    # Pending requests always float to the top, regardless of sort column
    # clicked — that's the whole point of this screen: "what needs me to
    # act on it right now", not a plain activity log.
    list_display = [
        "status_badge",
        "user",
        "plan_name",
        "amount",
        "method",
        "transaction_reference",
        "proof_thumb",
        "created_at",
    ]
    list_display_links = ["user", "plan_name"]
    list_filter = [
        "status",
        "method",
        "subscription__plan__exam",
    ]
    search_fields = [
        "user__email",
        "user__username",
        "transaction_reference",
        "subscription__plan__name",
    ]
    date_hierarchy = "created_at"
    list_per_page = 50

    actions = [approve_payments, reject_payments]

    readonly_fields = ["proof_preview", "created_at", "updated_at"]
    fieldsets = (
        (None, {
            "fields": ("user", "subscription", "amount", "method", "status"),
        }),
        ("Submitted by student", {
            "fields": ("transaction_reference", "proof_preview", "notes"),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    STATUS_COLORS = {
        "pending": "#a8823a",
        "approved": "#3f9142",
        "rejected": "#a8514d",
        "refunded": "#6b7280",
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related(
            "user", "subscription__plan__exam",
        )
        return qs.annotate(
            _pending_first=Case(
                When(status="pending", then=0),
                default=1,
                output_field=IntegerField(),
            )
        ).order_by("_pending_first", "-created_at")

    def plan_name(self, obj):
        return f"{obj.subscription.plan.exam.name} · {obj.subscription.plan.name}"
    plan_name.short_description = "Plan"
    plan_name.admin_order_field = "subscription__plan__name"

    def status_badge(self, obj):
        color = self.STATUS_COLORS.get(obj.status, "#6b7280")
        return format_html(
            '<span style="display:inline-block;padding:3px 10px;border-radius:999px;'
            'font-size:11px;font-weight:600;letter-spacing:.03em;text-transform:uppercase;'
            'color:#fff;background:{}">{}</span>',
            color, obj.get_status_display(),
        )
    status_badge.short_description = "Status"
    status_badge.admin_order_field = "status"

    def proof_thumb(self, obj):
        if not obj.proof_image:
            return "—"
        return format_html(
            '<a href="{0}" target="_blank" rel="noopener" title="Open full screenshot">'
            '<img src="{0}" style="width:44px;height:44px;object-fit:cover;'
            'border-radius:6px;border:1px solid #444;" /></a>',
            obj.proof_image.url,
        )
    proof_thumb.short_description = "Proof"

    def proof_preview(self, obj):
        if not obj.proof_image:
            return "No screenshot uploaded."
        return format_html(
            '<a href="{0}" target="_blank" rel="noopener">'
            '<img src="{0}" style="max-width:420px;max-height:420px;'
            'border-radius:8px;border:1px solid #444;" /></a>',
            obj.proof_image.url,
        )
    proof_preview.short_description = "Proof screenshot"