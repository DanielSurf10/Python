import json
from translate import Translator
traduzir = Translator(from_lang="Portuguese", to_lang="English", secret_access_key='59a0945cb4b0e849c1ab', pro=True)

with open("en_us.json", 'r') as arq:
    dic = json.loads(arq.read())

a = 0
for k, v in dic.items():
    print(f'{k:<50} - {traduzir.translate(v)}')
    a += 1

    if a == 21:
        break
