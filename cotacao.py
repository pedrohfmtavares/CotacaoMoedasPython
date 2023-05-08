# IMPORTANDO AS BIBLIOTECAS
import requests
from tkinter import *


# FUNÇÃO DE PEGAR OS VALORES DAS COTAÇÕES
def pegar_valores():

    # VARIÁVEL QUE RECEBE O METÓDO QUE BUSCA AS INFORMAÇÕES DAS COTAÇÕES DAS MOEDAS
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_valores["text"] = texto


# ABRINDO A JANELA INTERATIVA E DANDO TÍTULO PARA ELA
janela = Tk()
janela.title("Cotação do Dólar/Euro/BTC")


# COLOCANDO O TEXTO INICIAL NA TELA
texto_inicial = Label(janela, text="Clique no botão abaixo para exibir informações sobre as cotações do Dólar/Euro/BTC")
texto_inicial.grid(column=0, row=0, padx=10, pady=10)


# COLOCANDO O BOTÃO DE CLIQUE AQUI QUE RECEBE A FUNÇÃO DE PEGAR COTAÇÃO DAS MOEDAS
botao = Button(janela, text="Clique Aqui", command=pegar_valores)
botao.grid(column=0, row=1, padx=10, pady=10)


# COLOCANDO O TEXTO QUE EXIBE OS VALORES DAS COTAÇÕES DAS MOEDAS EM TEMPO REAL
texto_valores = Label(janela, text="")
texto_valores.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()