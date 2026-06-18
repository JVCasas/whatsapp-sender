import os
from dotenv import load_dotenv
import requests

load_dotenv()

zId:str = os.getenv('ZAPI_ID')
zToken:str = os.getenv('ZAPI_TOKEN')
zClientToken:str = os.getenv('ZAPI_CLIENT_TOKEN')

def sendMessage(phone:str, message:str):
    url = f'https://api.z-api.io/instances/{zId}/token/{zToken}/send-text'
    payload = {"phone": phone, "message": message}
    header = {"Client-Token": zClientToken, "Content-Type": "application/json"}

    try:
        response = requests.post(url, json = payload, headers = header)
        
        response.raise_for_status()

        print(response.json())
    
    except requests.exceptions.RequestException as e:
        print('Erro ao enviar mensagem!')
        print(e)

# Função que recebe um nome e um número de telefone e envia uma mensagem de saudação.
def sendGreeting(name:str, phone:str):
    message = f'Olá, {name} tudo bem com você?'
    try:
        sendMessage(phone, message)
    except:
        print('Erro ao enviar saudação.')