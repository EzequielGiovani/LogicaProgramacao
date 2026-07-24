import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def button_command():
    messagebox.showinfo(
        "Informação",
        "Você clicou no botão!"
    )

botao = tk.Button(
    root,
    text="Clique aqui",
    command=button_command()
)

botao.pack()

root.mainloop()