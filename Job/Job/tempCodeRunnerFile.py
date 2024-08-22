import requests
def skillApi():
    skill = input("enter skill :- ")
    url = f"https://api.apilayer.com/skills?q={skill}"

    payload = {}
    headers= {
    "apikey": "C40W9yqv1lSmkddZqFtNZpNx6NZPfBFM"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    print(result)

skillApi()