from pandas_datareader import data as web
import requests
import pandas as pd

tickers = ['ITSA4', 'B3SA3', 'OIBR4', 'QBTC11', 'CASH3']

def busca_cotacao():
    
    from datetime import date
    
    cotacao = []
    cont = 0
    hoje = date.today()
    texto = []
    
# Criando o DataFrame planilha
    planilha = pd.DataFrame()
    lista = ['Ticker', 'Data Compra', 'Data cotação', 'Cotação Abertura', 'Cotação Fechamento', 'Variação', 'Valor Pago', 'Lucro/Prejuízo', '% Lucro/Prejuízo']
    for i in lista:
        planilha[i] = " "
        print(f'Inserindo {i} no DataFrame planilha')
        
# Buscando as cotações e inserindo no DataFrame
    for ticker in tickers:
        print(f'Buscando a Cotação de: {ticker}')
        cotacao.append(web.DataReader(f'{ticker}.SA', data_source = 'yahoo', start = '01/01/2022' , end = hoje))
        data_compra = " "
        data_cotacao = hoje
        cotacao_abertura = cotacao[cont].Close[-1]
        cotacao_fechamento = cotacao[cont].Close[-1]
        variação = (cotacao_abertura - cotacao_fechamento) 
        valor_pago = 0
        lucro_prejuizo = valor_pago - cotacao_fechamento
        porc_lucro_prejuizo = (valor_pago / cotacao_fechamento) * 100
        
        cont += 1
        print(f'{ticker} | {data_compra} | {data_cotacao} | {cotacao_abertura} | {cotacao_fechamento} | {variação} | {valor_pago} | {lucro_prejuizo} | {porc_lucro_prejuizo}')
    return planilha

busca_cotacao()
