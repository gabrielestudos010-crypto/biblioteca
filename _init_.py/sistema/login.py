#importa a biblioteca customtkinter
from cProfile import label

import customtkinter as ctk

from sistema.inicial import exibi_inicial


def exibir_login():#função de exibir login

    app = ctk.CTk()
    app.title('login do usuario')
    app.geometry('300x300')
    ctk.set_appearance_mode('dark')#"system","dark,"light"

    def validacao_login():

        usuario = campo_usuario.get()
        senha = campo_senha.get()
        if usuario == "admin" and senha == "1234":
            app.destroy()
            exibi_inicial()
        else:
            print("senha ou usuario não localizado")

    #label e campo do usuario
    label_usuario = ctk.CTkLabel(app, text='usuario')
    label_usuario.pack(pady=(30, 0))

    campo_usuario = ctk.CTkEntry(app, placeholder_text='digite seu login')
    campo_usuario.pack(pady=5)

    #label e campo da senha
    label_senha = ctk.CTkLabel(app, text='senha')
    label_senha.pack(pady=(10, 0))

    campo_senha = ctk.CTkEntry(app, placeholder_text='digite sua senha')
    campo_senha.pack(pady=5)

    #label e campo do butom
    


    app.mainloop()