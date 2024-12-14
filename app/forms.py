from django import forms
from .models import Usuario, Telefone

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
        }

    
class FormularioTelefone(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['numero']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone'}),
        }
    
