from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from .forms import ContatoForm
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            celular = form.cleaned_data['celular']
            mensagem = form.cleaned_data['mensagem']

            assunto = f"Nova mensagem de {nome}"
            corpo = f"{mensagem}\n\nE-mail: {email}\nCelular: {celular}"

            send_mail(assunto, corpo, settings.EMAIL_HOST_USER, ['deckgamer7@gmail.com'], fail_silently=False)

            messages.success(request, 'Mensagem enviada!')
            form = ContatoForm()  # limpa o formulário
    else:
        form = ContatoForm()

    return render(request, 'portifolio/home.html', {'form': form})
