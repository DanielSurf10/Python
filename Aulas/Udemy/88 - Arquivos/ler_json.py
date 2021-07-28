import json

with open("en_us.json", 'r') as arq:
    dic = json.loads(arq.read())

for k, v in dic.items():
    print(f'{k:<75} - {v}')
