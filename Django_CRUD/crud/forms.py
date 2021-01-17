from django import forms

class UserForm(forms.Form):
    tracking_no= forms.CharField(max_length=100)
    
