from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    client = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='projects/'
    )

    description = models.TextField()

    completion_date = models.DateField()

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title