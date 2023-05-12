FROM python:latest

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

WORKDIR /src/ecommerce

COPY requirements.txt /src/ecommerce/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /src/ecommerce/
