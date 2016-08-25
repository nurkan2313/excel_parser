from django import forms
from models import Goods

class UploadFileForm(forms.Form):
    file = forms.FileField()