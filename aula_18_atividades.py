import tkinter as tk
from tkinter import messagebox

def enviar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()

    # Imprime os dados na console
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular: {celular}")
    
    # Opcional: mostrar confirmação para o usuário
    messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")

# Cria a janela principal
root = tk.Tk()
root.title("Formulário Cliente")

# Cria e posiciona os rótulos e campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_idade = tk.Entry(root, width=40)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="E-mail:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_endereco = tk.Entry(root, width=40)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Celular:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_celular = tk.Entry(root, width=40)
entry_celular.grid(row=4, column=1, padx=10, pady=5)

# Botão Enviar
botao_enviar = tk.Button(root, text="Enviar", command=enviar)
botao_enviar.grid(row=5, column=0, columnspan=2, pady=10)

# Inicia o loop da interface
root.mainloop()


# import tkinter as tk
# from tkinter import messagebox




# def display():
#     nome = nome_digitado.get()
#     idade = idade_digitada.get()
#     if nome and idade:
#         MOSTRAR_NOME.config(text=nome)
#         MOSTRAR_IDADE.config(text=idade)
#     else:
#        messagebox.showerror('isso é um erro', 'você não digitou nada')