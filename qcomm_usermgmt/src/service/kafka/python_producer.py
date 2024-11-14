from pykafka import KafkaClient as k_client
from datetime import datetime
import json



client = k_client(hosts="localhost:9092")

topic =  client.topics['testing']
producer = topic.get_sync_producer()
for i in range(0,1000):
    b =  json.dumps({'id':i,'name':f"name_{i}"}).encode('utf-8')
    producer.produce(message="Hello Sample".encode())
    print("Sending")