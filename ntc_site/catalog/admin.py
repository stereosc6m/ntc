from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'image',
    )
    list_editable = (
        'text',
        'image',
    )    
    list_filter = ('created_at',)
    list_display_links = ('title',)

admin.site.register(Product, ProductAdmin) 