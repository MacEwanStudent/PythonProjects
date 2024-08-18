import requests
from mylib.myinfo import MyInfo
import yaml
import datetime

today = datetime.date.today()
print(today.strftime("%Y%m%d"))
pixela_endpoint = "https://pixe.la/v1/users"
my_keys = MyInfo()
pixela_auth_token= my_keys.get_info("Pixea","AUTH_TOKEN")
pixela_user_name = my_keys.get_info("Pixea", "USER_NAME")

user_params = {
    "token": pixela_auth_token,
    "username": pixela_user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config ={
    "id":"graph1",
    "name":"Studying Python",
    "unit":"hour",
    "type":"float",
    "color": "shibafu"
}
headers= {
    "X-USER-TOKEN": pixela_auth_token
}
graph_endpoint = f"{pixela_endpoint}/{pixela_user_name}/graphs"

# response= requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response)
graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2"
}
graph_edit_endpoint = f"{pixela_endpoint}/{pixela_user_name}/graphs/graph1"

# response= requests.post(url=graph_edit_endpoint, json=graph_update, headers=headers)
# print(response.text)