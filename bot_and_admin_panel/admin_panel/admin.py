from django.contrib import admin

from core.models import Text, User


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text']


@admin.register(User)
class UserleAdmin(admin.ModelAdmin):
    search_fields = ['first_interaction', 'user_id']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
