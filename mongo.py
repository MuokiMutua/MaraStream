from pymongo import MongoClient # pip install pymongo
from confluent_kafka import Consumer
import json

# Mongo Connection
client = MongoClient('mongodb://localhost:27017/')
db = client['analytics_db']
collection = db['live_transactions']

# Kafka Consumer (Note: Different group.id)
c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mongo-group', 'auto.offset.reset': 'earliest'})
c.subscribe(['nairobi_transactions'])

while True:
    msg = c.poll(1.0)
    if msg:
        data = json.loads(msg.value().decode('utf-8'))
        collection.insert_one(data)