from azure.identity import ClientSecretCredential
import os
from azure.eventhub import EventHubConsumerClient
from azure.eventhub import EventData
from postgress_funcs import createOrUpdateTransaction

sec ="fUK8Q~h~ns-oSVzYUaA5FlNLXzZYxKnVpmnwnbXL"

credential =  ClientSecretCredential(tenant_id="d73f6f5b-ef95-47df-92d1-c327390691b0",
                             client_id="2b809f53-439a-4432-9378-40b14314116e",client_secret=sec)


def handle_event(partition_context, event:EventData):
    print("Received event from partition {}".format(partition_context.partition_id))
    partition_context.update_checkpoint(event)
    data =  event.body_as_json()
    print(data)
    try:
            trans_id = int(data['trs_id'])
            trs_name = str(data['Name']).upper()
            trs_status = str(data['Status']).upper()
            trs_type = str(data['Type']).upper()
            print(trans_id)
            createOrUpdateTransaction(transId=trans_id,TransName=trs_name,TransStatus=trs_status,TransType=trs_type)
    except Exception as e:
         print(e)

FULLY_QUALIFIED_NAMESPACE = "devtest243.servicebus.windows.net" #os.environ["EVENT_HUB_HOSTNAME"]
EVENTHUB_NAME = "testing243" #os.environ['EVENT_HUB_NAME']

consumer_client = EventHubConsumerClient(
    fully_qualified_namespace=FULLY_QUALIFIED_NAMESPACE,
    consumer_group='$Default',
    eventhub_name=EVENTHUB_NAME,
    credential=credential,
)

with consumer_client:
    consumer_client.receive(on_event=handle_event,starting_position=-1)