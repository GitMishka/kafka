import kafka
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send('your_topic_name', {'key': 'value'})

producer.flush()

producer.close()

