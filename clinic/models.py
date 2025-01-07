from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Service(models.Model):
    """
    Represents a service offered by the clinic, including its name,
    description, active status, slug for URLs, and timestamps.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter the name of the service."
    )
    description = models.TextField(
        help_text="Provide a brief description of the service."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to deactivate this service."
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text="Auto-generated from the service name."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the service as its string representation.
        """
        return self.name

    def clean(self):
        """
        Validates the service fields to ensure proper data integrity.
        """
        if not self.name.strip():
            raise ValidationError("Service name cannot be blank.")
        if len(self.name) > 100:
            raise ValidationError("Service name cannot exceed 100 characters.")

    def save(self, *args, **kwargs):
        """
        Saves the service instance and generates a unique slug if not set.
        """
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
