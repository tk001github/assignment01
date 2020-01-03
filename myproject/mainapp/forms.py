from django import forms
from .models import uploaded

class UploadForm(forms.ModelForm):
    class Meta:
        model = uploaded
        fields = ('charfield','filefield',)

      