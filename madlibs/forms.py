from django.forms import ModelForm
from .models import Madlib

class MadlibForm(ModelForm):
	class Meta:
		model = Madlib
		fields = ['title','text']