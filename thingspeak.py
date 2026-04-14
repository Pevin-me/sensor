import requests

API_KEY = "YOUR_WRITE_API_KEY"

url = "https://api.thingspeak.com/update"

data = {
    "api_key": API_KEY,
    "field1": 25,
    "field2": 60
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Data sent successfully!")
else:
    print("Failed to send data:", response.status_code)