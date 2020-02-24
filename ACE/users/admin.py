from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserRole
from .forms import UserRegisterForm
from import_export.admin import ImportExportModelAdmin 

admin.AdminSite.site_header = "Admin"
admin.AdminSite.site_title = "Site admin"
admin.AdminSite.index_title = "site adminstration"

@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin):

    list_display = ('__str__', 'first_name', 'last_name', 'role', 'department_id', 'is_active', 'last_login')
    list_display_links = ('__str__',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    list_per_page = 10
    search_fields = ('email',)
    empty_value_display = '-empty-'
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    radio_fields = {"gender": admin.HORIZONTAL}
    readonly_fields = tuple()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'mobile',
            'gender',
            'date_Of_birth',
            'department_id',
            'role',
            'profile_pic',
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        ('Important dates', {'fields': (
            'last_login',
            'date_joined',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    class Meta:
        model = CustomUser

admin.site.register(UserRole)
