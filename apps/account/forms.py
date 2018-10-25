from django import forms

from .models import Subscriber


class SubscriberAddForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    firstName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'})
    )
    secondName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'second name'})
    )

    class Meta:
        model = Subscriber
        fields = ('email', 'firstName', 'secondName')

