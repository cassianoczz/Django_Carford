from django.db import models
from django.core.exceptions import ValidationError


def restrict_amount(value):
    if Car.objects.filter(owner__id=value).count() >= 3:
        raise ValidationError('Owner already has maximal cars')


class Owner(models.Model):
    name = models.CharField(max_length=256)
    sale_opportunity = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.__class__.__name__} <{self.id}>: {self.name}"
    
    def save(self, *args, **kwargs):
        if Car.objects.filter(owner__id=self.id).count() == 0:
            self.sale_opportunity = True
        else:
            self.sale_opportunity = False
        return super().save(*args, **kwargs)


class Car(models.Model):
    MODELS_CARS = [
        ('Hatch', 'Hatch'),
        ('Sedan', 'Sedan'), 
        ('Convertible', 'Convertible'),
    ]
    COLORS_CARS = [
        ('Yellow', 'Yellow'),
        ('Blue', 'Blue'), 
        ('Gray', 'Gray'),
    ]

    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, validators=(restrict_amount, ))
    model = models.CharField(max_length=256, choices=MODELS_CARS)
    color = models.CharField(max_length=256, choices=COLORS_CARS)

    class Meta:
        ordering = ['owner__name']
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}<{self.owner.name}>: {self.model} ({self.color})"

    def save(self, *args, **kwargs):
        if Car.objects.filter(owner=self.owner).count() >= 0:
            self.owner.sale_opportunity = False
        self.owner.save()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if Car.objects.filter(owner=self.owner).count() <= 1:
            self.owner.sale_opportunity = True
        self.owner.save()
        return super().delete(*args, **kwargs)




