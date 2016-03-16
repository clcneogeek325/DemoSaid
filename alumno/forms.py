from django import forms
from .models import alumno

class alumnoForm(forms.ModelForm):
	class Meta:
		model = alumno
		fields = '__all__'
