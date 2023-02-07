import requests

endpoint = "https://www.httpbin.org/anything"

get_response = requests.get(endpoint)

print(get_response.json())