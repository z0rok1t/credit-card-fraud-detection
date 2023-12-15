from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class DatasetUploadForm(forms.Form):
    dataset_file =forms.FileField()