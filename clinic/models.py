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


class ServiceOption(models.Model):
    """
    Represents specific options for a service, such as duration, price,
    and a unique description to differentiate the options.
    """
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='options'
    )
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Price in Euro(€)"
    )
    description = models.TextField(
        help_text="A unique description for this service option"
    )

    def __str__(self):
        return f"{self.service.name} - {self.duration} mins"

    def clean(self):
        if self.duration <= 0:
            raise ValidationError("Duration must be a positive number.")
        if self.price <= 0:
            raise ValidationError("Price must be a positive number.")
        if self.description.strip() == "":
            raise ValidationError("Option description cannot be empty.")


class Masseuse(models.Model):
    """
    Represents a masseuse in the clinic with gender information.
    """
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def clean(self):
        """
        Validates that name and gender are not blank.
        """
        if not self.name.strip():
            raise ValidationError("Name cannot be blank.")
        if not self.gender.strip():
            raise ValidationError("Gender must be selected.")

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()})"
