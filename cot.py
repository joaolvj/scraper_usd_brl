from datetime import datetime

def get_url(url):
    """Faz a requisição a API do BC e retorna os dados em texto."""
    try:
        import requests
    except ModuleNotFoundError:
        print('Erro: o módulo "requests" não está instalado.')
        exit(1)
    try:
        # Faz a requisição a API do BC e guarda o conteúdo em uma variável
        response = requests.get(url)
        data = response.text
    except Exception as error:
        print(f'Erro: {error}')
    else:
        return data

def fetch_current_conversion(content):
    """Filtra a tag <taxaVenda> do XML resgatado e retorna o valor dela."""
    try:
        from bs4 import BeautifulSoup, FeatureNotFound
        # Inicia o módulo BeautifulSoup
        soup = BeautifulSoup(content, 'xml')
    except ModuleNotFoundError:
        print('Erro! o módulo "BeautifulSoup" não está instalado.')
        exit(1)
    except FeatureNotFound:
        print('Erro! Você não possuí um interpretador de XML válido instalado!')
    else:
        # Filtra o arquivo XML para puxar o valor de venda do dolár em real
        conversion = soup.find(name='taxaVenda')
        return conversion

def display_conversion():
    """Mostra o resultado formatado, com a data atual e valor do dólar em real."""
    data_atual = datetime.now()
    data_atual_formatada = data_atual.strftime('%Y-%m-%d')

    api_url = f'https://www3.bcb.gov.br/bc_moeda/rest/cotacao/fechamento/ultima/1/220/{data_atual_formatada}'

    data = get_url(api_url)
    conversion = fetch_current_conversion(data)

    print(f'Resultados de: {data_atual.strftime("%d/%m/%Y")}')
    print(f'Valor de compra do dólar: R$ {conversion.text[:-6]}')
