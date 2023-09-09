import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione a Pasta")

lista_arquivo = os.listdir(caminho)

locais = {
    "Imagens": [".png",".JPG", ".jpeg",".bmp", ".psd", ".tiff", ".gif"],
    "Planilhas": [".xls", ".xlsx",".xlm",".csv",".ods"],
    "PDFs": [".pdf"],
    "RAR ou ZIP": [".RAR",".ZIP", ".zip", ".rar", ".iso"],
    "Word": [".doc",".docx"],
    "Programas": [".exe",".msi",".bat"],
    "Videos": [".mp4",".mov",".wmv"],
    "Audios": [".mp3",".wav"],
    }

for arquivo in lista_arquivo:
    # 01. Arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")    
                                      