FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]