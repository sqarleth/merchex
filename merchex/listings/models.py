from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Band(models.Model):

    # Return name of fields instead of id in admin view
    def __str__(self):
        return f'{self.name}'

    # Set a dropdown list
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    # Set fields in table "Band"
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):

    def __str__(self):
        return f'{self.title}'

    class Type(models.TextChoices):
        Disques = "Records"
        Vetements = "Clothing"
        Affiches = "Posters"
        Divers = "Miscellaneous"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(blank=True, validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    type = models.fields.CharField(choices=Type.choices, max_length=50)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
