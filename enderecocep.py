from unicodedata import name
import requests


def main():
    print('## Consultar CEP ##\n')

    cep = input('Digite o CEP da sua cidade: ')
    if len(cep) != 8:
        print('CEP Invalido')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    res = request.json()

    if 'erro' not in res:

        # print(res)
        print('CEP: {}' .format(res['cep']))
        print('Logradouro: {}' .format(res['logradouro']))
        print('Complemento: {}' .format(res['complemento']))
        print('Bairro: {}' .format(res['bairro']))
        print('Localidade: {}' .format(res['localidade']))
        print('UF: {}' .format(res['uf']))
        print('IBGE: {}' .format(res['ibge']))
        print('GIA: {}' .format(res['gia']))
        print('DDD: {}' .format(res['ddd']))
        print('Siafi: {}' .format(res['siafi']))

    else:
        print('CEP não encontrado {}' .format(cep))


if __name__ == '__main__':
    main()
