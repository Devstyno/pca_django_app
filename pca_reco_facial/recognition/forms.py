from django import forms
from .models import Face

class FaceUploadForm(forms.ModelForm):
    class Meta:
        model = Face
        fields = ['name', 'image']
