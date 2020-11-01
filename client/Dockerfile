FROM python:3.8

RUN mkdir /app
COPY requirements.txt /app/.
WORKDIR /app
RUN apt-get update &&\
    apt install curl -y

RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
VOLUME /app
EXPOSE 8000
CMD ["python", "manage.py", "0.0.0.0:8000"]
