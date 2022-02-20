import requests

BASE = 'http://127.0.0.1:5000/'

#response = requests.get(BASE + "income-types")
#response = requests.get(BASE + "expense-types")
response = requests.post(BASE + "employees/82626")
print(response.json())