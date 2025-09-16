from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
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

admin.site.register(News, NewsAdmin) 
