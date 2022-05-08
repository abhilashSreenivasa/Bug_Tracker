from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import UserProfile,Role

class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'role', 'is_staff')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', )

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
# Register your models here.
admin.site.register(UserProfile,AccountAdmin)
admin.site.register(Role)

