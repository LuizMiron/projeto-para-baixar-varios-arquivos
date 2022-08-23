import requests
import os


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print(f'Download finalizado Salvo em: {os.path.abspath(endereco)}')
    else:
        resposta.raise_for_status()


if __name__ == '__main__':
    baixar_arquivo('https://ocw.mit.edu/ans7870/resources/Strang/Edited/Calculus/Calculus.pdf', 'teste.pdf')
