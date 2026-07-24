import tkinter as tk

root = tk.Tk()

root.geometry("400x300")

root.minsize(300, 200)
root.maxsize(800, 600)

root.attributes("-alpha", 0.8) #de 0 a 1

message = tk.Label(root, text=" ASHDBASHBDABDAHSDB AHB HBASDHBS HBDA HSB ABS YDABSUDYASB UYB")

message.pack()

root.mainloop()