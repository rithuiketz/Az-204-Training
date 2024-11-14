from pykafka import KafkaClient as k_client

client = k_client(hosts="localhost:9092")

topic =  client.topics['testing']


consumer  = topic.get_balanced_consumer(consumer_group="testing")
for message in consumer:
    print(message.value)

