import requests
import http.client
import sys
from get_auth_token import get_auth_token

user = str(sys.argv[1])
password = str(sys.argv[2])
client_secret = str(sys.argv[3])
controllerId = str(sys.argv[4])
valve = str(sys.argv[5])


print ('User = ' + user + ' ; controller ID  = ' + controllerId + ' ; valve = ' + valve)

conn = http.client.HTTPSConnection("api.hydrawise.com")
token = get_auth_token(user, password, client_secret)
querystring = {"appVersion":"hydrawise-web-client"}

payload = "[\n  {\n    \"operationName\": \"updateControllerMasterValve\",\n    \"variables\": {\n      \"zoneNumber\": " + valve + ",\n      \"controllerId\": " + controllerId + "\n    },\n    \"query\": \"mutation updateControllerMasterValve($zoneNumber: Int!, $controllerId: Int!) {\\n  updateControllerMasterValve(\\n    zoneNumber: $zoneNumber\\n    controllerId: $controllerId\\n  ) {\\n    ...zoneMasterValveFields\\n    __typename\\n  }\\n}\\n\\nfragment zoneMasterValveFields on MasterValve {\\n  zoneNumber {\\n    value\\n    label\\n    options {\\n      value\\n      label\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\"\n  }\n]\n"

headers = {
        "authorization": "Bearer " + str(token),
        "referer": "https://api.hydrawise.com/config/zones",
        "content-type": "application/json"
    }

conn.request("POST", "/api/v2/graph?appVersion=hydrawise-web-client", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
