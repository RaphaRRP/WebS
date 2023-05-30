import requests
from bs4 import BeautifulSoup
import create


def iniciar(produto_escolhido):
 
    print(produto_escolhido)

    url_base = 'https://www.colombo.com.br/produto/Smartphone-e-Celular/'

    response = requests.get(url_base + produto_escolhido)

    site = BeautifulSoup(response.text, 'html.parser')

    produtos = site.findAll('a', attrs={'class': 'styles__ContainerStyled-sc-rcmkij-1 xNjZO'})

    create.delete()
    create.criar_tabela('colombo.' + produto_escolhido)

    lista_primaria = []
   
    for produto in produtos:

        titulo = produto.find('h2')

        real = produto.find('span', attrs={'class': 'price'})

        centavos = produto.find('span', attrs={'class': 'sufix'})


        print('Título do produto: ', titulo.text)

        if(real):

            if(centavos):
                print('Preço do produto: ', real.text + centavos.text)
                valor = real.text + centavos.text

            else:
                print('Preço do produto: ', real.text)
                valor = real.text
        
        else:
            print('Produto indispovivel')
            valor = 'indisponível'

        tabela = produto_escolhido
        modelo = titulo.text

        create.create(tabela, modelo, valor)


        lista_secundaria = []
        lista_secundaria.append(modelo)
        lista_secundaria.append(valor)
        lista_primaria.append(lista_secundaria)

        print('\n\n')

    return lista_primaria

