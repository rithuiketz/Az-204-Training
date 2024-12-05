sec ="fUK8Q~h~ns-oSVzYUaA5FlNLXzZYxKnVpmnwnbXL"
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.identity import DefaultAzureCredential,ClientSecretCredential


credential =  ClientSecretCredential(tenant_id="d73f6f5b-ef95-47df-92d1-c327390691b0",
                             client_id="2b809f53-439a-4432-9378-40b14314116e",client_secret=sec)
#token = id.get_token('api://2b809f53-439a-4432-9378-40b14314116e/.default')


fully_qualified_namespace = "qcomm-mgmt-rith.servicebus.windows.net"
queue_name = "testing243"


with ServiceBusClient(fully_qualified_namespace, credential) as client:
    with client.get_queue_receiver(queue_name, max_wait_time=30,sub_queue="deadletter") as receiver:
        for msg in receiver:  # ServiceBusReceiver instance is a generator.
            print(str(msg))