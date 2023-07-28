from django.db import models

# Create your models here.

class Input (models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name
