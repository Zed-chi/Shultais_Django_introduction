from django import forms
from .models import Order
from houses.models import House


class OrderForm(forms.ModelForm):
    house = forms.ModelChoiceField(
        queryset=House.objects.all(), widget=forms.HiddenInput()
    )

    class Meta:
        model = Order
        fields = ["house", "name", "phone"]
