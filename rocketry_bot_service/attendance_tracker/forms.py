from django import forms

class MemberRegistryForm(forms.Form):
    """Handles forms"""
    full_name = forms.CharField(label="Your first and last name", max_length=60)
    email = forms.EmailField(label="Your rose-hulman email", max_length=64)
    snowflake = forms.CharField(max_length=32)
    user = forms.CharField(max_length=32)
    password = forms.CharField(max_length=96, widget=forms.PasswordInput())