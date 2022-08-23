import requests


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)


if __name__ == '__main__':
    baixar_arquivo('https://ocw.mit.edu/ans7870/resources/Strang/Edited/Calculus/Calculus.pdf', 'teste.pdf')
