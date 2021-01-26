from django import forms

class UploadFileForm(forms.Form):
    fileXls = forms.FileField()
