import os
import requests
from dotenv import load_dotenv

load_dotenv()

zapi = os.getenv('ZAPI')

def sendMessage():
    payload = {"phone": "5521988670501", "message": 'Olá mundo'}
    header = {"Client-Token": zapi, "Content-Type": "application/json"}

    response = requests.post(zapi, json = payload, headers = header)

    print(response.text)

sendMessage()