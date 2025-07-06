from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Seu nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'seu@email.com'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escreva sua mensagem...'}))