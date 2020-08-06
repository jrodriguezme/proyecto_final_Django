from django import forms
from .models import Usuario

class Enter(forms.ModelForm):
    class Meta:
    	password = forms.CharField(widget=forms.PasswordInput)
        model = Usuario
        fields = [
			'id_user',
			'username',
			'password',
		]