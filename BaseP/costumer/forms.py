from django import forms
from costumer.models import Cliente

class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
