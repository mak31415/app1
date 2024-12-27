from django.contrib import admin
from carts.admin import CartTabAdmin

from users.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_editable = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    fields = (
        'username',
        'email',
        'is_staff',
        'is_active',
    )

    inlines = [CartTabAdmin,]