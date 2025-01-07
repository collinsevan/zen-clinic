from django.contrib import admin
from .models import Service, ServiceOption


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Service model.
    """
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at')


@admin.register(ServiceOption)
class ServiceOptionAdmin(admin.ModelAdmin):
    """
    Admin interface for managing service options.
    """
    list_display = ('service', 'duration', 'price', 'description')
    search_fields = ('service__name', 'description')
    list_filter = ('service',)
