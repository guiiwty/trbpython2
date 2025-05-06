import os
import shutil

def coletar_dados():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")
    return f"Nome: {nome}\nIdade: {idade}\nEmail: {email}\n"

def salvar_txt(dados, nome_arquivo="dados.txt"):
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write(dados + "\n")
    print(f"[OK] Dados salvos em {nome_arquivo}")

def criar_binario(origem="dados.txt", destino="dados.bin"):
    with open(origem, "rb") as f_orig, open(destino, "wb") as f_dest:
        shutil.copyfileobj(f_orig, f_dest)
    print(f"[OK] Cópia binária criada como {destino}")

def ler_binario_e_reconstruir(binario="dados.bin"):
    with open(binario, "rb") as f:
        conteudo = f.read().decode("utf-8")
    return conteudo

def exibir_arquivos():
    print("\n--- CONTEÚDO ORIGINAL (.txt) ---")
    with open("dados.txt", "r", encoding="utf-8") as f:
        print(f.read())

    print("\n--- CONTEÚDO RECONSTRUÍDO DO .bin ---")
    print(ler_binario_e_reconstruir())

def main():
    print("=== SISTEMA DE COLETA DE DADOS ===")
    while True:
        dados = coletar_dados()
        salvar_txt(dados)

        mais = input("Deseja adicionar mais dados? (s/n): ").lower()
        if mais != "s":
            break

    criar_binario()
    exibir_arquivos()
    print("\nOs arquivos 'dados.txt' e 'dados.bin' foram salvos no diretório atual.")

if __name__ == "__main__":
    main()
