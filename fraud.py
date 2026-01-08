from confluent_kafka import Consumer
import json

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'fraud-detector-group',
    'auto.offset.reset': 'earliest'
})
c.subscribe(['nairobi_transactions'])

print("🛡️ Fraud Detector Active: Monitoring for > 100,000 KES...")

while True:
    msg = c.poll(1.0)
    if msg:
        data = json.loads(msg.value().decode('utf-8'))
        amount = data['amount']
        
        if amount > 100000:
            print(f"🚨 ALERT: Suspicious high-value transaction!")
            print(f"ID: {data['tx_id']} | Amount: {amount} KES | Merchant: {data['merchant']}")
            # In a real app, you would send an SMS or Email here.