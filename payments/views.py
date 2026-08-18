from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from .models import Payment, Subscription, SubscriptionPlan
from .serializers import (
    SubscriptionPlanSerializer,
    SubscriptionSerializer,
    PaymentCreateSerializer,
    PaymentSerializer,
)


class SubscriptionPlanListView(generics.ListAPIView):
    """
    GET /api/payments/plans/?exam=mdcat

    Returns active subscription plans.
    """
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = (
            SubscriptionPlan.objects
            .filter(
                is_active=True,
                exam__is_active=True,
            )
            .select_related("exam")
        )

        exam_slug = self.request.query_params.get("exam")

        if exam_slug:
            qs = qs.filter(exam__slug=exam_slug)

        return qs


class MySubscriptionListView(generics.ListAPIView):
    """
    GET /api/payments/subscriptions/

    Returns the authenticated student's subscriptions.
    """
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Subscription.objects
            .filter(user=self.request.user)
            .select_related("plan__exam")
            .order_by("-created_at")
        )


class MyActiveSubscriptionView(generics.GenericAPIView):
    """
    GET /api/payments/subscription/active/

    Returns the currently active subscription, if one exists.
    """
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        now = timezone.now()

        subscription = (
            Subscription.objects
            .filter(
                user=request.user,
                status="active",
                expires_at__gt=now,
            )
            .select_related("plan__exam")
            .order_by("-expires_at")
            .first()
        )

        if not subscription:
            return Response(
                {"active": False, "subscription": None},
                status=200,
            )

        return Response({
            "active": True,
            "subscription": SubscriptionSerializer(subscription).data,
        })

class PaymentCreateView(generics.CreateAPIView):
    """
    POST /api/payments/payments/

    Creates a pending payment and a pending subscription.
    """

    serializer_class = PaymentCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @transaction.atomic
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        plan = get_object_or_404(
            SubscriptionPlan,
            id=serializer.validated_data["plan_id"],
            is_active=True,
        )

        subscription = Subscription.objects.create(
            user=request.user,
            plan=plan,
            status="pending",
        )

        payment = Payment.objects.create(
            user=request.user,
            subscription=subscription,
            amount=plan.price,
            method=serializer.validated_data["method"],
            transaction_reference=serializer.validated_data.get(
                "transaction_reference",
                "",
            ),
            proof_image=serializer.validated_data.get("proof_image"),
            notes=serializer.validated_data.get("notes", ""),
            status="pending",
        )

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED,
        )    