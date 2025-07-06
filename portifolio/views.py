from django.core.mail import send_mail
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
            corpo = f"{nome} tem um recado para voçê: '{mensagem}' E-mail: {email} Celular: {celular}"

            send_mail(assunto, corpo, settings.EMAIL_HOST_USER, ['decknho@hotmail.com'], fail_silently=False)
            return render(request, 'portifolio/contato_enviado.html')
    else:
        form = ContatoForm()

    return render(request, 'portifolio/home.html', {'form': form})
