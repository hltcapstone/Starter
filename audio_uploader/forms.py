from django import forms

class UploadAudioForm(forms.Form):
	file = forms.FileField()
