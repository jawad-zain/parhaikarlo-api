from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user_email', 'primary_exam', 'current_class', 'target_year', 'city', 'created_at')
    list_filter = ('primary_exam', 'current_class', 'is_email_verified')
    search_fields = ('full_name', 'user__email', 'user__username', 'phone')
    readonly_fields = ('created_at', 'updated_at')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'