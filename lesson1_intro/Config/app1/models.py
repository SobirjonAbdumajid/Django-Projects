from django.db import models

class Maqola(models.Model):
    LOCAL = 'local'
    WORLD = 'world'
    SPORT = 'sport'
    TAG = (
        (LOCAL, 'Staff'),
        (WORLD, 'Guest'),
        (SPORT, 'Manager'),
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    tag = models.CharField(max_length=15, choices=TAG, blank=True, null=True)
    rank = models.CharField(max_length=50)  # Add appropriate max_length
    age = models.IntegerField(blank=True, null=True)  # Add age field if used in views
    address = models.CharField(max_length=255, blank=True, null=True)  # Correct field name

    @property
    def imageURL(self):
        return self.image.url if self.image else ''

    def __str__(self):
        return f'{self.id}. {self.name}'
