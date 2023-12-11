import requests

url = "https://httpbin.org/basic-auth/admin/admin"

payload = {}
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)