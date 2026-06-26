from django.db import models


class Quotation(models.Model):

    STATUS_CHOICES = (
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Closed', 'Closed'),
    )

    BUILDING_TYPES = (
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Hospital', 'Hospital'),
        ('Industrial', 'Industrial'),
    )

    LIFT_TYPES = (
        ('Passenger Lift', 'Passenger Lift'),
        ('Hospital Lift', 'Hospital Lift'),
        ('Home Lift', 'Home Lift'),
        ('Glass Lift', 'Glass Lift'),
        ('Goods Lift', 'Goods Lift'),
        ('Capsule Lift', 'Capsule Lift'),
    )

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    city = models.CharField(max_length=100)

    lift_type = models.CharField(
        max_length=100,
        choices=LIFT_TYPES
    )

    building_type = models.CharField(
        max_length=100,
        choices=BUILDING_TYPES
    )

    floors = models.PositiveIntegerField()

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.lift_type}"
