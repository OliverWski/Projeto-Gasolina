#Importa bibliotecas
from baixa_arquivos import dados_gasolina
from baixa_dados_senado import dados_senado
from trata_csv import trata

if __name__ == '__main__':
    
    mes_inicial = str(input("Digite o mês por extenso: "))
    mes_final = str(input("Digite o mês por extenso: "))
    
    dados_gasolina(mes_inicial, mes_final)
    
    trata()
    
    dados_senado(mes_inicial, mes_final)
    