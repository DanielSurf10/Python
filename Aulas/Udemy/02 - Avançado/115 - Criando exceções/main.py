class TaErradoError(Exception):
    pass


def func():
    raise TaErradoError("Errado")


try:
    func()
except TaErradoError as error:
    print(f"Erro: {error}")
