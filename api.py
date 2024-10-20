from flask import Flask, request
from kafka import KafkaProducer

app = Flask(__name__)

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/send', methods=['POST'])
def send_data():
    data = request.json['data']
    producer.send('api_trial', value=data.encode('utf-8'))
    producer.flush()
    return f"Data '{data}' sent to Kafka topic 'api_trial'."

if __name__ == "__main__":
    app.run(port=5000)
