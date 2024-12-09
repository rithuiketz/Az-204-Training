from azure.identity import ClientSecretCredential
import os
from azure.eventhub import EventHubProducerClient
from azure.eventhub import EventData

from json import dump,dumps

sec ="fUK8Q~h~ns-oSVzYUaA5FlNLXzZYxKnVpmnwnbXL"

credential =  ClientSecretCredential(tenant_id="d73f6f5b-ef95-47df-92d1-c327390691b0",
                             client_id="2b809f53-439a-4432-9378-40b14314116e",client_secret=sec)


def handle_event(partition_context, event:EventData):
    print("Received event from partition {}".format(partition_context.partition_id))
    partition_context.update_checkpoint(event)
    print(event.body_as_json())

FULLY_QUALIFIED_NAMESPACE = "devtest243.servicebus.windows.net" #os.environ["EVENT_HUB_HOSTNAME"]
EVENTHUB_NAME = "testing243" #os.environ['EVENT_HUB_NAME'

producer_client:EventHubProducerClient = EventHubProducerClient(
    fully_qualified_namespace=FULLY_QUALIFIED_NAMESPACE,
    consumer_group='$Default',
    eventhub_name=EVENTHUB_NAME,
    credential=credential,
)


body = dumps({"trs_id":123,"Name":"R","Type":"Purchase","Status":"cancel"}).encode()
with producer_client:
    producer_client.send_event(event_data=EventData(body))
    print("Sent")