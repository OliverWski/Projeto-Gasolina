def dados_senado(mes_inicial, mes_final):
    
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from urllib.request import Request, urlopen
    from urllib.request import urlretrieve
    
    #Cria dicionario com base no mes solicitado pelo usuario
    lista_meses = [('Janeiro', '01'),('Fevereiro', '02'),('Marco', '03'),('Abril', '04'),('Maio', '05'),('Junho', '06'),('Julho', '07'),('Agosto', '08'),('Setembro', '09'),('Outubro', '10'),('Novembro', '11'),('Dezembro', '12')]
    meses = dict(lista_meses)
    primeira_pesquisa = meses.get(mes_inicial)
    segunda_pesquisa = meses.get(mes_final)
    
    ano = '2022'
    pesquisa = [primeira_pesquisa, segunda_pesquisa]
    cards = []

    #URL o qual será trabalhada
        
    response = urlopen('https://www12.senado.leg.br/noticias/materias/2022/01/lista/')
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    pages = 15

    #Itens dentro do site
    for y in pesquisa:
        for i in range(pages):  
            url = ('https://www12.senado.leg.br/noticias/materias/2022/' + str(y) + '/lista/' + str(i + 1))
            response = urlopen(url)
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            print(url + " Referente ao mês: " + y)
            
            #Implementa o dicionario para popular o arquivo em csv e passa por cada informação requisitida na pagina
            
            anuncios = soup.find('div', {"id": "textoMateria"}).findAll('div', {"class": "border-bottom-d d-flow-root"})
            
            for anuncio in anuncios:
                card = {}
                
                card['Materia'] = anuncio.find('span', {'class': 'eta normalis-xs'}).getText()
                card['Tipo'] = anuncio.find('span', {'class': 'normalis'}).getText()
                card['Data'] = anuncio.find('div', {'class': 'text-muted normalis hidden-xs'}).getText()
                                
                cards.append(card)
            
        #Popula o arquivo em csv    
        dataset = pd.DataFrame.from_dict(cards)
        dataset.to_csv(r'./output/dataset.csv', sep=';', index = False, encoding = 'utf-8-sig')

    print("Finalizado")