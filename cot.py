from datetime import datetime

def get_url(url):
    """Faz a requisição a API do BC e retorna os dados em texto."""
    try:
        import requests
    except ModuleNotFoundError:
        print('\nErro: o módulo "requests" não está instalado.'
        '\nInstale o pacote "requests" com o pip!\n')
        exit(1)
    try:
        # Faz a requisição a API do BC e guarda o conteúdo em uma variável
        response = requests.get(url)
        data = response.text
    except Exception as error:
        print(f'\nErro: {error}')
    else:
        return data

def fetch_current_conversion(content, verbose=False):
    """Filtra a tag <taxaVenda> do XML resgatado e retorna o valor dela."""
    try:
        from bs4 import BeautifulSoup, FeatureNotFound
        # Inicia o módulo BeautifulSoup
        soup = BeautifulSoup(content, 'xml')
    except ModuleNotFoundError:
        print('\nErro! o módulo "BeautifulSoup" não está instalado.\n'
              'Instale o pacote "bs4" com o pip!\n')
        exit(1)
    except FeatureNotFound:
        print('\nErro! Você não possuí um interpretador de XML válido instalado!'
              'Instale o pacote "lxml" com o pip!\n')
        exit(1)
    else:
        # Filtra o arquivo XML para puxar o valor de venda do dolár em result
        if verbose:
            extra_info = []
            seller_tax = soup.find(name='taxaVenda')
            buyer_tax = soup.find(name='taxaCompra')
            is_from_buletin = soup.find(name='cotacaoBoletim')
            extra_info.append(seller_tax)
            extra_info.append(buyer_tax)
            extra_info.append(is_from_buletin)
            return extra_info
        else:
            conversion = soup.find(name='taxaVenda')
            return conversion



def display_conversion(url, verbose=False):
    """Mostra o resultado formatado, com a data atual e valor do dólar em result."""
    current_date = datetime.now()
    current_date_formatted = current_date.strftime('%Y-%m-%d')

    api_url = url + current_date_formatted

    data = get_url(api_url)

    # Se o programa rodar como o argumento de verbosidade, mostrará mais informações sobre a atualização
    if verbose:
        conversion = fetch_current_conversion(data, verbose=True)
        result = conversion[1].text[:-4]
        print('-'*38)
        print(f'Resultados de: {current_date.strftime("%d/%m/%Y")}'.center(38))
        print('-'*38)
        print(f'É uma cotação do boletim? -> {conversion[2].text}')
        print(f'Valor de compra do dólar -> R$ {conversion[0].text[:-4]}'.replace('.', ','))
        print(f'Valor de venda do dólar -> R$ {result}'.replace('.', ','))
        print('-'*38)
    else:
        conversion = fetch_current_conversion(data)
        result = conversion.text[:-6]
        print(f'R$ {result}'.replace('.', ','))
    return float(result)