from django import forms
from .models import Usuario

class Enter(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
			'id_user',
			'username',
			'password',
		]