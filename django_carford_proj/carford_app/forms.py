from carford_app.models import Owner, Car

from django import forms


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'