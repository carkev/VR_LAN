FROM python:latest

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

WORKDIR /www/ecommerce

COPY requirements.txt /www/ecommerce/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /www/ecommerce/
COPY venv/Lib/site-packages/sphinxdoc /usr/local/lib/python3.11/site-packages/sphinxdoc
