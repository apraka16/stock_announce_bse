import requests

endpoint = "http://localhost:8000/api/stocks/"

get_response = requests.get(endpoint)

print(get_response.json())