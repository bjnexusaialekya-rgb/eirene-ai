import requests

url = "http://localhost:8000/chat"

payload = {
    "message": "I feel lonely"
}

response = requests.post(url, json=payload)

print(response.json())
