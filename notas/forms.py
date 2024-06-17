from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome_razao_social'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control', 'id': 'cnpj_cpf'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'id': 'cep'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'id': 'endereco'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'id': 'bairro'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'id': 'municipio'}),
            'uf': forms.Select(attrs={'class': 'form-select', 'id': 'estado'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control', 'id': 'inscricao_estadual'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'id': 'descricao'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantidade'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control', 'id': 'valor_unitario'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control', 'id': 'valor_total'}),
        }
