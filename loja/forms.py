from django import forms
from django.forms import ModelForm
from .models import Usuario, Produto, Fornecedor, SavedItem


#Testendo Forms

class SavedItemForm(forms.ModelForm):
    class Meta:
        model = SavedItem
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do item'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        }

#Fim teste Forms
class UsuarioForm(ModelForm):
    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={
            "class": "input",
            "type": "text",
            "placeholder": "Digite seu nome",
        })
    )
    sobrenome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input",
            "type": "text",
            "placeholder": "Digite seu sobrenome",
        })
    )
    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input",
            "type": "text",
            "placeholder": "Digite seu cpf",
        })
    )
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input",
            "type": "number",
            "placeholder": "Digite seu telefone",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "input",
            "type": "email",
            "placeholder": "Digite seu email",
        })
    )
    endereco = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input",
            "type": "text",
            "placeholder": "Digite seu endereço",
        })
    )

    class Meta:
        model = Usuario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'telefone',
            'email',
            'endereco',
        ]

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome', 
            'preco', 
            'descricao', 
            'quantidadeEstoque', 
            'foto', 
            'loja', 
        ]

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'cnpj', 
            'nome', 
            'telefone', 
            'email', 
            'endereco', 
        ]

