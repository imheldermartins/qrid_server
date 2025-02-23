FROM python:3.14.0a5-slim-bullseye

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV PYTHONPATH=/app

# Definir o diretório de trabalho
WORKDIR /app

# **Instalar dependências do sistema antes de instalar os pacotes Python**
RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential python3-dev

# Copiar e instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o restante do código do projeto para o contêiner
COPY . /app/

# Comando para iniciar o servidor Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]

# Expor a porta que o servidor usará
EXPOSE ${PORT}
