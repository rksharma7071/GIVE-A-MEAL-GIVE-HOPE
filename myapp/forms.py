from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donator_name', 'food_type', 'quantity', 'expiry_date', 'pickup_time', 'pickup_location']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pickup_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
        }
        labels = {
            'donator_name': 'Donator Name',
            'food_type': 'Food Type',
            'expiry_date': 'Expiry Date',
            'pickup_time': 'Pickup Time',
            'pickup_location': 'Pickup Location',
        }
        # help_texts = {
        #     'donator_name': 'Enter your name or restaurant name',
        #     'quantity': 'Enter the quantity of food in kgs/lbs',
        #     'pickup_location': 'Enter the pickup location',
        # }
        error_messages = {
            'donator_name': {
                'required': 'This field is required',
            },
            'food_type': {
                'required': 'This field is required',
            },
            'quantity': {
                'required': 'This field is required',
            },
            'expiry_date': {
                'required': 'This field is required',
            },
            'pickup_time': {
                'required': 'This field is required',
            },
            'pickup_location': {
                'required': 'This field is required',
            },
        }

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
