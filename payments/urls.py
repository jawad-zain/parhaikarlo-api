from django.urls import path
from .views import (
    SubscriptionPlanListView,
    MySubscriptionListView,
    MyActiveSubscriptionView,
    PaymentCreateView,
)

urlpatterns = [
    path(
        "plans/",
        SubscriptionPlanListView.as_view(),
        name="subscription-plan-list",
    ),
    path(
        "subscriptions/",
        MySubscriptionListView.as_view(),
        name="my-subscriptions",
    ),
    path(
        "subscription/active/",
        MyActiveSubscriptionView.as_view(),
        name="my-active-subscription",
    ),
    path(
        "payments/",
        PaymentCreateView.as_view(),
        name="payment-create",
    ),
]