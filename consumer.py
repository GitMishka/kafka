from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'your_topic_name',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(f"Received message: {message.value}")

consumer.close()
