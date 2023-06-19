import tkinter as tk
from tkinter import ttk
import WebScraping
from tkinter import *
from connect import cursor, data_base
import pandas as pd
from openpyxl import Workbook
import conversor


def btn1_click():
    print("Botão 1 clicado")
    produto_escolhido = 'Samsung'
    WebScraping.iniciar(produto_escolhido)
    lista = WebScraping.iniciar(produto_escolhido)
    carregar_dados(lista)
    criar_tabela(produto_escolhido)

def btn2_click():
    print("Botão 2 clicado")
    produto_escolhido = 'Motorola'
    WebScraping.iniciar(produto_escolhido)
    lista = WebScraping.iniciar(produto_escolhido)
    carregar_dados(lista)
    criar_tabela(produto_escolhido)


def btn3_click():
    print("Botão 3 clicado")
    produto_escolhido = 'Nokia'
    WebScraping.iniciar(produto_escolhido)
    lista = WebScraping.iniciar(produto_escolhido)
    carregar_dados(lista)
    criar_tabela(produto_escolhido)

def btn4_click():
    print("Botão 4 clicado")
    produto_escolhido = 'Apple'
    WebScraping.iniciar(produto_escolhido)
    lista = WebScraping.iniciar(produto_escolhido)
    carregar_dados(lista)
    criar_tabela(produto_escolhido)

def btn5_click():
    print("Botão 5 clicado")
    produto_escolhido = 'Xiaomi'
    WebScraping.iniciar(produto_escolhido)
    lista = WebScraping.iniciar(produto_escolhido)
    carregar_dados(lista)
    criar_tabela(produto_escolhido)

def carregar_dados(lista):
    window = tk.Tk()
    window.destroy()
    window = tk.Tk()
    dados = lista
    tv = ttk.Treeview(window, columns=('modelo', 'valor'), show='headings')
    tv.column('modelo', minwidth=0, width=750)
    tv.column('valor', minwidth=0, width=100)
    tv.heading('modelo', text='modelo')
    tv.heading('valor', text='valor')
    tv.pack()

    for (modelo, valor) in dados:
        tv.insert("", "end", values=(modelo, valor))



def criar_tabela(produto_escolhido):
    dados = WebScraping.iniciar(produto_escolhido)

    dados_com_cabecalho = [["Marca: " + produto_escolhido, "Preço"]] + dados

    df = pd.DataFrame(dados_com_cabecalho[1:], columns=dados_com_cabecalho[0])

    arquivo_excel = "dados.xlsx"
    writer = pd.ExcelWriter(arquivo_excel, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for column_cells in worksheet.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        worksheet.column_dimensions[column_cells[0].column_letter].width = length + 2

    writer._save()

    print("Tabela exportada para o arquivo:", arquivo_excel)

    conversor.converter()



window = tk.Tk()

btn1 = tk.Button(window, text="Samsung", command=btn1_click)
btn2 = tk.Button(window, text="Motorola", command=btn2_click)
btn3 = tk.Button(window, text="Nokia", command=btn3_click)
btn4 = tk.Button(window, text="Apple", command=btn4_click)
btn5 = tk.Button(window, text="Xiaomi", command=btn5_click)


btn1.pack(side=tk.RIGHT)
btn2.pack(side=tk.RIGHT)
btn3.pack(side=tk.RIGHT)
btn4.pack(side=tk.RIGHT)
btn5.pack(side=tk.RIGHT)



window.mainloop()