from django.contrib import admin
from django.utils import timezone
from datetime import timedelta

from .models import Payment, Subscription, SubscriptionPlan


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


@admin.action(description="Approve selected payments")
def approve_payments(modeladmin, request, queryset):
    now = timezone.now()

    for payment in queryset.select_related("subscription__plan"):
        if payment.status != "pending":
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

    modeladmin.message_user(
        request,
        "Selected pending payments were approved.",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "subscription",
        "amount",
        "method",
        "status",
        "transaction_reference",
        "created_at",
    ]
    list_filter = [
        "status",
        "method",
        "subscription__plan__exam",
    ]
    search_fields = [
        "user__email",
        "user__username",
        "transaction_reference",
    ]
    ordering = ["-created_at"]

    actions = [approve_payments]