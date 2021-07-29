import json

dicionario = {
    "Pessoa 1": {
        'nome': "João",
        'idade': 15
    },
    "Pessoa 2": {
        'nome': "Maria",
        'idade': 11
    }
}

with open("pessoas.json", "w") as arq:
    arq.write(json.dumps(dicionario, indent=True))
