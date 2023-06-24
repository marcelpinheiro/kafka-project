from confluent_kafka import Consumer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import json
import time

# Kafka configuration
kafka_broker = 'localhost:9092'
kafka_topic = 'crypto_data'

# Elasticsearch configuration
es_scheme = 'http'  # or 'https' if applicable
es_host = 'localhost'
es_port = 9200
es_index = 'crypto_data_index'

# Elasticsearch client
es_client = Elasticsearch(
    hosts=[{'host': es_host, 'port': es_port, 'scheme': es_scheme}],
    headers={'Content-Type': 'application/json'}
)

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': kafka_broker,
    'group.id': 'crypto_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Kafka consumer
consumer = Consumer(consumer_config)
consumer.subscribe([kafka_topic])


def consume_and_index():
    while True:
        message = consumer.poll(1.0)  # Poll for messages with a timeout of 1.0 second

        if message is None:
            continue

        if message.error():
            print(f"Consumer error: {message.error()}")
            continue

        crypto_data = json.loads(message.value().decode('utf-8'))
        actions = [
            {
                '_index': es_index,
                '_source': {
                    'symbol': crypto_data['symbol'],
                    'price': crypto_data['price'],
                    'timestamp': int(time.time())
                }
            }
        ]

        # Use the bulk function to efficiently index the documents
        bulk(es_client, actions)
        print(f"Cryptocurrency data indexed in Elasticsearch index '{es_index}'")

    consumer.close()


try:
    # Start consuming messages from Kafka and indexing in Elasticsearch
    consume_and_index()
except KeyboardInterrupt:
    pass
finally:
    # Close the Kafka consumer
    consumer.close()
