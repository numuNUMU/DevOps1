FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY flask-app .

EXPOSE 5000
CMD [ "python3", "app.py"]
