FROM python:3.10.6

# Não utilizar arquivos .pyc na construção da imagem/container
ENV PYTHONDONTWRITEBYTECODE 1

# Os logs de erro não se perdem entre a aplicação e o container
ENV PYTHONUNBUFFERED 1

WORKDIR /e_commerce_app

COPY . /e_commerce_app/ 

RUN pip install -U pip
RUN pip install -r requirements.txt
