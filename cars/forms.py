from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    is_featured = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'style': 'margin-right: 10px;'
    }))

    class Meta:
        model = Car
        fields = [
            'car_title', 'state', 'city', 'color', 'model', 
            'year', 'condition', 'price', 'description', 
            'car_photo', 'car_photo_1', 'car_photo_2', 
            'car_photo_3', 'car_photo_4', 'features', 
            'body_style', 'engine', 'transmission', 
            'interior', 'miles', 'doors', 'passengers',
            'vin_no', 'milage', 'fuel_type', 'no_of_owners',
            'is_featured'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all form fields
        for field in self.fields:
            if field not in ['features', 'is_featured']:
                self.fields[field].widget.attrs['class'] = 'form-control'
            elif field == 'features':
                self.fields[field].widget.attrs.update({
                    'class': 'form-check-input',
                    'style': 'margin-right: 10px;'
                })