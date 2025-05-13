import os
import shutil
import tkinter as tk
from tkinter import messagebox

def coletar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    return f"Nome: {nome}\nIdade: {idade}\nEmail: {email}\n"

def salvar_txt(dados, nome_arquivo="dados.txt"):
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write(dados + "\n")
    messagebox.showinfo("Sucesso", f"[OK] Dados salvos em {nome_arquivo}")

def criar_binario(origem="dados.txt", destino="dados.bin"):
    with open(origem, "rb") as f_orig, open(destino, "wb") as f_dest:
        shutil.copyfileobj(f_orig, f_dest)
    messagebox.showinfo("Sucesso", f"[OK] Cópia binária criada como {destino}")

def exibir_arquivos():
    try:
        with open("dados.txt", "r", encoding="utf-8") as f:
            conteudo_txt = f.read()
        conteudo_bin = ler_binario_e_reconstruir()
        messagebox.showinfo("Conteúdo dos Arquivos", 
                            f"CONTEÚDO ORIGINAL (.txt):\n{conteudo_txt}\n\nCONTEÚDO RECONSTRUÍDO DO .bin:\n{conteudo_bin}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def ler_binario_e_reconstruir(binario="dados.bin"):
    with open(binario, "rb") as f:
        conteudo = f.read().decode("utf-8")
    return conteudo

def coletar_e_salvar():
    dados = coletar_dados()
    salvar_txt(dados)

def criar_e_exibir():
    criar_binario()
    exibir_arquivos()

root = tk.Tk()
root.title("Sistema de Coleta de Dados")

tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Idade:").grid(row=1, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

btn_coletar = tk.Button(root, text="Coletar e Salvar Dados", command=coletar_e_salvar)
btn_coletar.grid(row=3, column=0, columnspan=2)

btn_exibir = tk.Button(root, text="Criar Binário e Exibir Arquivos", command=criar_e_exibir)
btn_exibir.grid(row=4, column=0, columnspan=2)

root.mainloop()
