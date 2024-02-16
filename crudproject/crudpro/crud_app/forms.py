from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        labels = {
            'c_id': 'CUSTOMER ID',
            'f_name': 'FIRST NAME',
            'l_name': 'LAST NAME',
            'product': 'PRODUCT NAME',
            'price': 'PRICE'
        }