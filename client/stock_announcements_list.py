import requests

endpoint = "http://localhost:8000/api/stocks/500112"

get_response = requests.get(endpoint)

print(get_response.json())