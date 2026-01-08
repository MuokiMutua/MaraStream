import json
import time
import random
from confluent_kafka import Producer

# Configuration
conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(conf)

merchants = ['Naivas', 'Quickmart', 'Carrefour', 'Zucchini']
locations = ['Westlands', 'Kilimani', 'CBD', 'Karen']

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Success: {msg.topic()} [{msg.partition()}]")

print("Starting Transaction Stream...")

while True:
    payload = {
        "tx_id": f"TX{random.randint(1000, 9999)}",
        "amount": round(random.uniform(50, 150000), 2),
        "merchant": random.choice(merchants),
        "location": random.choice(locations),
        "currency": "KES",
        "timestamp": time.time()
    }
    
    producer.produce(
        'nairobi_transactions', 
        json.dumps(payload).encode('utf-8'), 
        callback=delivery_report
    )
    producer.poll(1)
    time.sleep(1) # Send 1 transaction every second