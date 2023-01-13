import os
import azure.identity
import azure.mgmt.resource

import azure.functions as func

import json
import requests

import json
from azure.eventhub import EventHubClient, EventData

import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Create an Azure IdentityClient using the default managed identity
    identity_client = azure.identity.IdentityClient()

    # Authenticate and get an access token
    token = identity_client.get_access_token("https://management.azure.com/")

    # Create an Azure Resource Management client using the access token
    credentials = azure.mgmt.resource.ResourceManagementClient(
        credentials=azure.identity.TokenCredential(token)
    )

    # Use the client to access a resource (in this case, a resource group)
    resource_group = credentials.resource_groups.get("my-resource-group")

    # Return the resource group name as the HTTP response
    return func.HttpResponse(resource_group.name)
  
  ###########
  
  
  def main(req: func.HttpRequest, my_property: func.Property) -> func.HttpResponse:
    value = my_property.get()
    return func.HttpResponse(f"The value of my_property is: {value}")

#####  
  
# Event Hub connection string
connection_str = 'Endpoint=sb://<eventhub_namespace>.servicebus.windows.net/;SharedAccessKeyName=<shared_access_key_name>;SharedAccessKey=<shared_access_key>;EntityPath=<eventhub_name>'

# Create an Event Hub client
client = EventHubClient.from_connection_string(connection_str)

# Receive events from the Event Hub
with client:
    receiver = client.add_receiver(partition_id="0", offset=Offset("-1"), prefetch=10)
    for event_data in receiver.receive(timeout=5):
        # Get the JSON data from the event
        json_data = json.loads(event_data.body_as_str())
        print(json_data)

# JSON data
data = {"property1": "value1", "property2": "value2"}

# Change the value of a property
data["property1"] = "new value"

# Convert the JSON data to a string
json_data = json.dumps(data)

# Send the POST request with the JSON data
response = requests.post("http://example.com/endpoint", json=json_data)

# Print the status code of the response
print(response.status_code)


#############

# Event Hub connection string
connection_str = 'Endpoint=sb://<eventhub_namespace>.servicebus.windows.net/;SharedAccessKeyName=<shared_access_key_name>;SharedAccessKey=<shared_access_key>;EntityPath=<eventhub_name>'

# Create an Event Hub client
client = EventHubClient.from_connection_string(connection_str)

# JSON data to send
data = {"property1": "value1", "property2": "value2"}
json_data = json.dumps(data)

with client:
    # Send the JSON data as an event to the Event Hub
    client.send(EventData(json_data))

# Close the connection
client.close()

# Azure Key Vault URL
key_vault_url = "https://<your-key-vault-name>.vault.azure.net"

# Create a DefaultAzureCredential object
credential = DefaultAzureCredential()

# Create a SecretClient object
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Get the secret
secret = client.get_secret("<secret-name>")

# Print the value of the secret
print(secret.value)

