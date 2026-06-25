# Create your models here.
from django.db import models
from django.utils.text import slugify


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('Passenger Lift', 'Passenger Lift'),
        ('Hospital Lift', 'Hospital Lift'),
        ('Home Lift', 'Home Lift'),
        ('Glass Lift', 'Glass Lift'),
        ('Goods Lift', 'Goods Lift'),
        ('Capsule Lift', 'Capsule Lift'),
        ('Automobile Lift', 'Automobile Lift'),
        ('MRL Lift', 'MRL Lift'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to='products/'
    )

    short_description = models.TextField()

    features = models.TextField(
        help_text="Enter features separated by commas"
    )

    capacity = models.CharField(
        max_length=100,
        help_text="Example: 6 Persons / 408 Kg"
    )

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title