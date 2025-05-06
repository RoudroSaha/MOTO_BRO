from django import forms

from .models import Car

class CarForm(forms.ModelForm): 
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'car_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car title'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter color'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter condition'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'features': forms.Select(attrs={'class': 'form-control'}),
            'body_style': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter body style'}),
            'engine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter engine details'}),
            'transmission': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter transmission'}),
            'interior': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter interior details'}),
            'miles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter miles'}),
            'doors': forms.Select(attrs={'class': 'form-control'}),
            'passengers': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter passenger capacity'}),
            'vin_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter VIN number'}),
            'milage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter mileage'}),
            'fuel_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter fuel type'}),
            'no_of_owners': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of owners'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }