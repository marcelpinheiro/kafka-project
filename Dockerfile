FROM python:3.9

WORKDIR /app

COPY requirements.txt .
# Update pip and install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "bitcoin_producer.py"]
