from django import forms

class ProfileImageForm(forms.Form):
	image = forms.FileField(label = "Select File")
