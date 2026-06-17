import requests

def sendMessage(zapiId:str, zapiToken:str, phone:str, message:str):
    url = f'https://api.z-api.io/instances/{zapiId}/token/{zapiToken}/send-text'
    payload = {"phone": phone, "message": message}
    header = {"Client-Token": url, "Content-Type": "application/json"}

    response = requests.post(url, json = payload, headers = header)

    print(response.text)
