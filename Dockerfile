FROM python:3.8.5-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /netguru_task
WORKDIR /netguru_task
COPY requirements.txt /netguru_task/
COPY . /netguru_task /netguru_task/
RUN pip install -r requirements.txt
