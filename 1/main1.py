import requests

response = requests.post('https://nodus.caseguru.ru/trainee/tasks', json={"task": 1, "result": "just practice"})
print(response.content)