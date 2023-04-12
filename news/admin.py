from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'pub_date', 'is_visible')
    list_filter = ('is_visible', 'pub_date')
    search_fields = ('title', 'url', 'description', 'text')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)


