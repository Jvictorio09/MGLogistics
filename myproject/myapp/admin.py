# myapp/admin.py
from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'subtitle', 'slug', 'is_active')
        }),
        ('Media & Files', {
            'fields': ('image', 'brochure_1', 'brochure_2')
        }),
        ('Service Content', {
            'fields': ('description', 'extra_info', 'bullets')
        }),
    )

from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
