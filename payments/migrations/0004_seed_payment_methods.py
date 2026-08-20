# Seeds the two payment methods that were, until now, hardcoded in the
# frontend (app/(app)/plans/upgrade/[planId]/page.tsx's METHODS array) —
# same label/instructions, just moved from JS bundle to admin-editable data.

from django.db import migrations


METHODS = [
    {
        'method': 'easypaisa',
        'label': 'EasyPaisa',
        'instructions': 'Send to 0321-3529795 · Jawad Zain',
        'order': 0,
    },
    {
        'method': 'sadapay',
        'label': 'SadaPay',
        'instructions': 'Send to 0321-3529795 · Jawad Zain',
        'order': 1,
    },
]


def seed_methods(apps, schema_editor):
    PaymentMethodOption = apps.get_model('payments', 'PaymentMethodOption')
    for data in METHODS:
        PaymentMethodOption.objects.update_or_create(
            method=data['method'],
            defaults={
                'label': data['label'],
                'instructions': data['instructions'],
                'order': data['order'],
                'is_active': True,
            },
        )


def unseed_methods(apps, schema_editor):
    PaymentMethodOption = apps.get_model('payments', 'PaymentMethodOption')
    PaymentMethodOption.objects.filter(
        method__in=[m['method'] for m in METHODS],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_paymentmethodoption'),
    ]

    operations = [
        migrations.RunPython(seed_methods, unseed_methods),
    ]
