from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'api_trial',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
