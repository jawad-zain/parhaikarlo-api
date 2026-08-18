from django.contrib import admin
from .models import BuildTask


@admin.register(BuildTask)
class BuildTaskAdmin(admin.ModelAdmin):
    list_display = ('week', 'title', 'is_done', 'order')
    list_filter = ('week', 'is_done')
    list_editable = ('is_done', 'order')
    search_fields = ('title', 'notes')
    ordering = ('week', 'order')