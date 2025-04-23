FROM python:3.11-slim

WORKDIR /App

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 4000

CMD ["python", "app.py"]

