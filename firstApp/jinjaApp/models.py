from django.db import models

# Create your models here.
class Cars(models.Model):
    CAR_TYPE_CHOICES = [
        ('SUV', 'Sports-Utility Vehicle'),
        ('MUV', 'Multi-Utility Vehicle'),
        ('CNV', 'Convertibles'),
        ('SED', 'Sedan'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    type = models.CharField(max_length=3, choices=CAR_TYPE_CHOICES)

    def __str__(self):
        return self.name
