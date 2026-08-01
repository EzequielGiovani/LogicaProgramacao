import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

root.mainloop()