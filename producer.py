from kafka import KafkaProducer
import pandas as pd
import time

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Read CSV file
df = pd.read_csv('heart_rate_data.csv')  # replace 'your_file.csv' with the path to your file

# Send rows one by one
for index, row in df.iterrows():
    data = str(row.iloc[0])  # Convert the value to a string using .iloc
    producer.send('api_trial', value=data.encode('utf-8'))  # Send the encoded string to Kafka
    print(f'Sent: {data}')
    time.sleep(1)  # Add delay if needed

producer.flush()
producer.close()