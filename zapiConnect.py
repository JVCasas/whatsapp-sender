import os
from dotenv import load_dotenv
import requests

load_dotenv()

zId:str = os.getenv('ZAPI_ID')
zToken:str = os.getenv('ZAPI_TOKEN')

def sendMessage(phone:str, message:str):
    url = f'https://api.z-api.io/instances/{zId}/token/{zToken}/send-text'
    payload = {"phone": phone, "message": message}
    header = {"Client-Token": url, "Content-Type": "application/json"}

    try:
        response = requests.post(url, json = payload, headers = header)
        
        response.raise_for_status()

        print(response.json())
    
    except requests.exceptions.RequestException as e:
        print('Erro ao enviar mensagem!')
        print(e)