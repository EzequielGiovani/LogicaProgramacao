import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Modifica o título que aparece no topo da janela
root.title("SSENAI - Desenvolvimento de Sistemas")

# Cria m rótulo (label) com o texto "Hello, World!"
message = tk.Label(root, text="Hello, World!")

message2 = tk.Label(root, text="Janela criada usando o Tkinter")

# Posiciona o rótulo na janela
message.pack()
message2.pack()

# Define o tamanho da janela (largura x altura + posicao x + posicao y)
root.geometry("1920x1080+0+0")

#inicia o loop principal da interface grafica
root.mainloop()