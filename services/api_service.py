import requests
from flask import current_app
from utils.helpers import deserialize_binary_response

# def get_admin_ids():
#     url = f"{current_app.config['API_URL']}/glAetAldminId"
#     response = requests.get(url, headers={"Content-Type": "application/json"})
#     if response.status_code == 200 :
#         print("Data get admin_id scucessfully")
#     else:
#         print("Failed to get data admin")
#     return response.json() if response.status_code == 200 else None

def get_event_ids():
    url = f"{current_app.config['API_URL']}/getAllEvent"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        print("Data get event_id successfully")
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to get data event_id: {str(e)}")
        return None

def get_user_ids(event_id):
    url = f"{current_app.config['API_URL']}/getUserId"
    headers = {"Content-Type": "application/json", "Create-by-id": str(event_id)}
    response = requests.get(url, headers=headers)
    if response.status_code == 200 :
        print("Data get user_id scucessfully")
    else:
        print("Failed to get data")
    return response.json() if response.status_code == 200 else None

def get_event_and_user_image(user_id,event_id):
    url = f"{current_app.config['API_URL']}/getEventFolderImage"
    headers = {"Content-Type": "application/json", "Create-by-id": str(event_id)}
    data = {"userId": user_id}
    response = requests.get(url, headers=headers, json=data)
    if response.status_code == 200 :
        print("Data get admin_id,get_event_id scucessfully")
    else:
        print("Failed to get data admin_id,get_event_id")
    getdata=deserialize_binary_response(response)
    print("Data:",getdata.json())
    return getdata.json() if response.status_code == 200 else None

def post_data(data_list):
    url = f"{current_app.config['API_URL']}/setuserEventImage"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data_list)
    if response.status_code == 200:
        print("Data posted successfully")
    else:
        print("Failed to post data")