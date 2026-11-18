import customtkinter as ctk
from sistema.livro import cadatrar_livro


def exibi_inicial():
    ini = ctk.CTk()
    ini.titli("pagina inicial - adm")
    ini.geometry("500x400")

    label_titulo = ctk.CTkLabel(ini, text="PAINEL DO BIBLIOTECARIO")
    label_titulo.pack(pady=30)

    btn_titulo = ctk.CTkButton(ini, text="cadastra leitor")
    btn_titulo.pack(pady=15)

    btn_titulo = ctk.CTkButton(ini, text="cadastrar livro", command=lambda:(cadastra_livro(ini)))
    btn_titulo.pack(pady=15)

    btn_titulo = ctk.CTkButton(ini, text="emprestimos")
    btn_titulo.pack(pady=15)

    ini.mainloop()