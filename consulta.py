# Importando as Bibliotecas
from pandas_datareader import data as web
import requests
import pandas as pd
from datetime import date

# Criando a lista dos ticker das ações 
tickers = ['ITSA4', 'OIBR4', 'CASH3']

# Criando o DataFrame com as informaões básicas
lista_2 = [['ITSA4', 100.0, 10.80, "03/25/2022"],
           ['OIBR4', 100.0, 1.38, "03/25/2022"],
           ['CASH3', 100.0, 2.49, "03/25/2022"]]
dados = pd.DataFrame(lista_2)
dados.columns = ['Ticker', 'Quantidade', 'VL_Compra', 'Data Compra']
dados

# Definindo a função buscar cotação
def busca_cotacao():
    
    cotacao = []
    cont = 0
    hoje = date.today()
    lista = ['Ticker', 'Data Compra', 'Data cotação', 'Abertura', 'Fechamento', 'Variação', 'Valor Pago', 'Quantidade', 'Lucro/Prejuízo', '% Lucro/Prejuízo']
    retorno = []
    
    # Buscando as cotações e inserindo na lista retorno
    for ticker in tickers:
        print(f'Buscando a Cotação de: {ticker}')
        cotacao.append(web.DataReader(f'{ticker}.SA', data_source = 'yahoo', start = '01/01/2022' , end = hoje))
        
        # Formatando data de Compra
        mes = dados[['Ticker', 'Data Compra']].set_index('Ticker').loc[ticker][0].split('/')[0]
        dia = dados[['Ticker', 'Data Compra']].set_index('Ticker').loc[ticker][0].split('/')[1]
        ano = dados[['Ticker', 'Data Compra']].set_index('Ticker').loc[ticker][0].split('/')[2]
        data_compra = (f'{dia}/{mes}/{ano}')
        
        # Formatando data da cotação
        ano = hoje.year
        mes = hoje.month
        dia = hoje.day
        data_cotacao = (f'{dia}/{mes}/{ano}')
        
        cotacao_abertura = cotacao[cont].Close[-2].round(2)
        cotacao_fechamento = cotacao[cont].Close[-1].round(2)
        variação = (f'{((cotacao_fechamento / cotacao_abertura)-1) * 100:.2f} %')
        valor_pago = dados[['Ticker', 'VL_Compra']].set_index('Ticker').loc[ticker][0]
        quantidade = dados[['Ticker', 'Quantidade']].set_index('Ticker').loc[ticker][0]
        lucro_prejuizo = (f'{(valor_pago * quantidade) - (cotacao_fechamento * quantidade):.2f}')
        porc_lucro_prejuizo = (f'{((cotacao_fechamento / valor_pago)-1) * 100:.2f} %')
        
        cont += 1
        
        # Criando uma lista com listas das cotações
        retorno.append([ticker, data_compra, data_cotacao, cotacao_abertura, cotacao_fechamento, variação, valor_pago, quantidade, lucro_prejuizo, porc_lucro_prejuizo])

    # Criando um DataFrame com o retorno e inserindo os rótulos das Colunas      
    planilha = pd.DataFrame(retorno)
    planilha.columns = lista
    planilha.set_index('Ticker', inplace=True)

    return planilha

# Chamando a função e armazenando na variável planilha
planilha = busca_cotacao()

# Exportando o DataFrame para um Arquivo .csv com a data da cotação no nome do arquivo
planilha.to_csv(f'cotacao_{hoje.day}-{hoje.month}-{hoje.year}.csv', encoding='utf-8')
planilha
