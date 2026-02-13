FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_DEBUG=1

# Port 5001 for insecure site, 5002 for jackpot site
EXPOSE 5001 5002
