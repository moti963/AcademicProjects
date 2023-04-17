from django.db import models

# Create your models here.


class Data(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}-{self.contact}"
