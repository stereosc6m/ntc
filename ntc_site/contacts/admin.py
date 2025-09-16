from django.contrib import admin

from .models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'text',
    )

    list_filter = ('created_at',)

admin.site.register(Request, RequestAdmin)