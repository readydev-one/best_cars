# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=datetime.now().year,
        validators=[MinValueValidator(2015), MaxValueValidator(datetime.now().year)]
    )
    
    # Fields to manage import tracking
    is_imported = models.BooleanField(default=False)
    last_synced = models.DateTimeField(null=True, blank=True)

    # You might also want an external ID for reference
    external_id = models.CharField(max_length=100, blank=True, null=True, unique=True)

    fuel_efficiency = models.DecimalField(
        max_digits=5, decimal_places=2, 
        blank=True, null=True,
        help_text="Fuel efficiency (e.g., miles per gallon or liters per 100km)"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, null=True,
        help_text="Listing price of the car"
    )
    image_url = models.URLField(
        max_length=500,
        blank=True, null=True,
        help_text="URL for the car image"
    )
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

