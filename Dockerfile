FROM python:3.9

WORKDIR /app

COPY requirements.txt .
# Update pip and install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . ./app

# Set the working directory
WORKDIR /app

CMD ["python", "bitcoin_producer.py"]

# Run a command that keeps the container running
CMD tail -f /dev/null
