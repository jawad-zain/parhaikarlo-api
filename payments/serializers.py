from rest_framework import serializers

from .models import Payment, Subscription, SubscriptionPlan


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    exam_name = serializers.CharField(
        source="exam.name",
        read_only=True,
    )

    class Meta:
        model = SubscriptionPlan
        fields = [
            "id",
            "exam",
            "exam_name",
            "name",
            "duration_days",
            "price",
            "is_active",
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = [
            "id",
            "plan",
            "starts_at",
            "expires_at",
            "status",
            "created_at",
        ]


class PaymentCreateSerializer(serializers.Serializer):
    plan_id = serializers.IntegerField()

    method = serializers.ChoiceField(
        choices=[
            "manual",
            "jazzcash",
            "easypaisa",
            "bank_transfer",
        ],
    )

    transaction_reference = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=True,
    )

    proof_image = serializers.ImageField(
        required=False,
        allow_null=True,
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True,
    )


class PaymentSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(
        source="subscription.plan.name",
        read_only=True,
    )

    class Meta:
        model = Payment
        fields = [
            "id",
            "subscription",
            "plan_name",
            "amount",
            "method",
            "transaction_reference",
            "status",
            "proof_image",
            "notes",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "subscription",
            "amount",
            "status",
            "created_at",
            "updated_at",
        ]