from django.contrib import admin
from .models import Service, ServiceOption, Masseuse, ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing service categories.
    """
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Service model.
    """
    list_display = (
        'name', 'category', 'is_active', 'created_at', 'updated_at'
    )
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at', 'category')


@admin.register(ServiceOption)
class ServiceOptionAdmin(admin.ModelAdmin):
    """
    Admin interface for managing service options.
    """
    list_display = ('service', 'duration', 'price', 'description')
    search_fields = ('service__name', 'description')
    list_filter = ('service',)


@admin.register(Masseuse)
class MasseuseAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Masseuse model.
    Displays name and gender. Includes filters and search.
    """
    list_display = ('name', 'gender')
    list_filter = ('gender',)
    search_fields = ('name',)
