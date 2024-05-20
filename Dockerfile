# syntax=docker/dockerfile:1
FROM python:3.12

COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app
CMD ["flask", "run", "-h", "0.0.0.0"]
EXPOSE 5000