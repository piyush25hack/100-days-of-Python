import requests
from datetime import datetime
USERNAME ="angela"
Token = "Your Token ID Here"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params ={
    "token": "TOKEN",
    "username": "USERNAME",
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

graph_endpoint =f"{pixela_endpoint}/" {USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response =requests.post(url = graph_endpoint, json= graph_config, headers = headers)
print(response.text)

pixel_creation_endpoint =f{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}
today = datetime.now()
#print(today.strftime("%Y%m%D"))
pixel_data ={
    "date": today.strftime("%Y%m%D"),
    "quantity":input("How many kilometers did you cycle today?"),
}
# response = requests.post(url= pixel_creation_endpoint, json =pixel_data, headers= headers)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%D')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json = new_pixel_data, headers = headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%D')}"
# response =requests.delete(url =delete_endpoint, headers= headers)
# print(response.text)