import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def registrar_log(mensagem):
    with open('log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: {mensagem}\n")

def organizar_arquivos(diretorio, criterio):
    if not os.path.exists(diretorio):
        print("O diretório não existe.")
        return

    tipos_arquivos = {
        'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'documentos': ['.pdf', '.docx', '.txt'],
        'videos': ['.mp4', '.avi'],
        'musicas': ['.mp3', '.wav'],
    }

    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_arquivo):
            if criterio == 'tipo':
                _, extensao = os.path.splitext(arquivo)
                movido = False

                for tipo, extensoes in tipos_arquivos.items():
                    if extensao.lower() in extensoes:
                        novo_diretorio = os.path.join(diretorio, tipo)
                        if not os.path.exists(novo_diretorio):
                            os.makedirs(novo_diretorio)

                        shutil.move(caminho_arquivo, os.path.join(novo_diretorio, arquivo))
                        registr_log(f'Movido: {arquivo} para {novo_diretorio}')
                        movido = True
                        print(f'Movido: {arquivo} para {novo_diretorio}')
                        break

                if not movido:
                    print(f'Não foi possível organizar: {arquivo}')
            elif criterio == 'data':
                data_criacao = os.path.getctime(caminho_arquivo)
                data_dir = datetime.fromtimestamp(data_criacao).strftime('%Y-%m-%d')

                novo_diretorio = os.path.join(diretorio, 'data', data_dir)
                if not os.path.exists(novo_diretorio):
                    os.makedirs(novo_diretorio)

                shutil.move(caminho_arquivo, os.path.join(novo_diretorio, arquivo))
                registrar_log(f'Movido: {arquivo} para {novo_diretorio}')
                print(f'Movido: {arquivo} para {novo_diretorio}')

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        criterio = criterio_var.get()
        organizar_arquivos(diretorio, criterio)
        messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")

def main():
    global criterio_var
    
    root = tk.Tk()
    root.title("Organizador de Arquivos")

    label = tk.Label(root, text="Escolha o critério de organização:")
    label.pack(pady=10)

    criterio_var = tk.StringVar(value='tipo')
    tipo_radio = tk.Radiobutton(root, text='Por Tipo de Arquivo', variable=criterio_var, value='tipo')
    tipo_radio.pack(anchor='w')
    
    data_radio = tk.Radiobutton(root, text='Por Data de Criação', variable=criterio_var, value='data')
    data_radio.pack(anchor='w')

    btn = tk.Button(root, text="Selecionar Diretório", command=selecionar_diretorio)
    btn.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
