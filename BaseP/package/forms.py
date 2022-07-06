from django import forms
from package.models import Paquete

class Paquete_form(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = '__all__'