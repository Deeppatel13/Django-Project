from django import forms
from .models import BookForm

class FormBookForm(forms.ModelForm):
    class Meta:
        model= BookForm
        fields= ["pickup_location", "drop_location", "mobile_no", "username","email"]