from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer
import requests
import json
import time

# Coinbase API URL for cryptocurrency prices
api_url = 'https://api.coinbase.com/v2/prices'

# List of cryptocurrency symbols
cryptocurrencies = ['BTC', 'ETH', 'LTC']  # Add more if desired

# Kafka configuration
kafka_broker = 'localhost:9092'
kafka_topic = 'crypto_data'
kafka_partition_count = 3
kafka_replication_factor = 3

# Kafka admin client
admin = AdminClient({'bootstrap.servers': kafka_broker})

# Create Kafka topic
topic = NewTopic(kafka_topic, num_partitions=kafka_partition_count, replication_factor=kafka_replication_factor)
admin.create_topics([topic])

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': kafka_broker
}

# Kafka producer
producer = Producer(producer_config)


def get_crypto_price(symbol):
    url = f'{api_url}/{symbol}-USD/spot'
    response = requests.get(url)
    data = response.json()

    if 'data' in data and 'amount' in data['data']:
        return data['data']['amount']
    else:
        return None


def produce_crypto_data(symbol):
    crypto_price = get_crypto_price(symbol)

    if crypto_price:
        # Produce cryptocurrency data to Kafka topic
        message = json.dumps({'symbol': symbol, 'price': crypto_price}).encode('utf-8')
        producer.produce(kafka_topic, value=message)
        producer.flush()
        print(f"Cryptocurrency data produced to Kafka topic '{kafka_topic}': {symbol} {crypto_price} USD")
    else:
        print(f"Failed to retrieve cryptocurrency data for symbol '{symbol}'")


# Fetch and produce cryptocurrency data every 5 seconds
while True:
    for symbol in cryptocurrencies:
        produce_crypto_data(symbol)
    time.sleep(5)  # Wait for 5 seconds before fetching again
