FROM python:3.8

COPY ./requirements-freeze.txt /requirements.txt
COPY ./personsearch /personsearch

WORKDIR /personsearch

RUN pip3 install -r /requirements.txt --no-cache-dir

EXPOSE 8000