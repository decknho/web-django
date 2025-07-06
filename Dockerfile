# Imagem leve com Python
FROM python:3.11-slim

# Define o diretório do app
WORKDIR /app

# Copia os arquivos do projeto
COPY . /app/

# Instala dependências no ambiente virtual
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install -r requirements.txt

# Adiciona o venv ao PATH
ENV PATH="/opt/venv/bin:$PATH"

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para rodar o projeto (ajuste se necessário)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
