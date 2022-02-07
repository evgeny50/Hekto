FROM python:3.10

WORKDIR /usr/src/hekto

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/hekto

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]