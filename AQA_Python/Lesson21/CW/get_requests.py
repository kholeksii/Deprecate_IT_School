import requests


def get():
    url = "https://httpbin.org/basic-auth/admin/admin"

    payload = {}
    headers = {
      'accept': 'application/json',
      'Authorization': 'Basic YWRtaW46YWRtaW4='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # отримуємо код!
    print(response.status_code)

get()