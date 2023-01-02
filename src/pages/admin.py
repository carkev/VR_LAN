"""...
"""
from django.contrib import admin
import gdpr_assist

from .models import Staff, StaffRole


# Register your models here.
class StaffRoleAdmin(admin.ModelAdmin):
    """...
    """
    list_display = ["name"]
    list_display_links = ["name"]


class StaffAdmin(gdpr_assist.admin.ModelAdmin):
    """...
    """
    list_display = ["firstname", "lastname", "mail", "picture", "staff_role"]
    list_display_links = ["firstname", "lastname", "mail", "picture",
                          "staff_role"]

admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffRole, StaffRoleAdmin)
