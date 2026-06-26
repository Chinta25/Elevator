from django.db import models


class Testimonial(models.Model):

    client_name = models.CharField(max_length=100)

    company = models.CharField(
        max_length=100,
        blank=True
    )

    designation = models.CharField(
        max_length=100,
        blank=True
    )

    photo = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True
    )

    feedback = models.TextField()

    rating = models.PositiveSmallIntegerField(default=5)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.client_name
