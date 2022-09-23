FROM python:3.9

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

COPY ./req.txt .
RUN pip3 install -r req.txt

COPY . .
