FROM python:3-alpine

WORKDIR /app

RUN pip install Flask
COPY flask-app .

EXPOSE 5000
CMD [ "python3", "app.py"]
