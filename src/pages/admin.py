"""...
"""
from django.contrib import admin

from .models import Staff, StaffRole


# Register your models here.
class StaffRoleAdmin(admin.ModelAdmin):
    """...
    """
    list_display = ["name"]
    list_display_links = ["name"]


class StaffAdmin(admin.ModelAdmin):
    """...
    """
    list_display = ["firstname", "lastname", "mail", "picture", "staff_role"]
    list_display_links = ["firstname", "lastname", "mail", "picture",
                          "staff_role"]

admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffRole, StaffRoleAdmin)
