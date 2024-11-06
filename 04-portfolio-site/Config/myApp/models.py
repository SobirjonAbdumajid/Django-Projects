from django.db import models

# Create your models here.
class MaqolaModel(models.Model):
    TAG = (
        ("Certificates", "Certificates"),
        ("Projects", "Projects"),
        ("Education", "Education"),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    source = models.CharField(max_length=255)
    link = models.CharField(max_length=500, blank=True, null=True)
    description_uzb = models.TextField(blank=True, null=True)
    description_eng = models.TextField(blank=True, null=True)
    tags = models.CharField(choices=TAG, max_length=255, blank=True, null=True)

    @property
    def imageURL(self):
        return self.image.url if self.image else ""

    def __str__(self):
        return self.title