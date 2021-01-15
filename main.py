import socket
import requests

webhookURL = '<webhook url>'
hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)

data = {
    'username': 'Server IP Webhook',
    'embeds': [{
        'title': 'Server started!',
        'description': hostname + ': ' + localIP,
    }]
}

result = requests.post(webhookURL, json = data)

try:
    result.raise_for_status()
except:
    pass