import argparse
import cot
# TODO Criar um módulo de formatação de moedas, para simplificar a função main abaixo
# import formatmoney

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--real', help='Valor usado para converter de real para dólar', type=float)
parser.add_argument('-d', '--dolar', help='Valor usado para converter de dólar para real', type=float)
parser.add_argument('-v', '--verbose', help='Aumenta a verbose do programa', action='store_true')

args = parser.parse_args()

# URL da API atual do Banco do Brasil
URL = f'https://www3.bcb.gov.br/bc_moeda/rest/cotacao/fechamento/ultima/1/220/'

def main():
    try:
        if args.verbose:
            result = cot.display_conversion(url=URL, verbose=True)
        else:
            result = cot.display_conversion(URL)
        if args.real:
            print(f'\nR$ {args.real:.2f} -> $ 1.00 = $ {args.real // result:.2f}'.replace('.', ','))
        if args.dolar:
            print(f'$ {args.dolar:.2f} -> R$ 1.00 = R$ {result * args.dolar:.2f}'.replace('.', ','))
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()
