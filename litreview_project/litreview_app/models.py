from django.db import models

class Ticket(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    image = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'