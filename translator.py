import requests
import uuid

# Add your key and endpoint
key = "cdb001451ed548d8aea92530cd96685d"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region. required if you're using a multiservice or regional (not global) resource. It can
# be found in the Azure portal on the Keys and Endpoint page.
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'es',
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multiservice or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4()),
}

# You can pass more than one object in body.
body = [{
    'text': "Doran's ring"
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
print(response)

print(response[0]['translations'][0]['text'])