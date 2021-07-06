FROM python:3-alpine

WORKDIR /app


RUN pip install flask==1.1.1 

COPY flask-app .

EXPOSE 8000

CMD ["python", "app.py"]
