import random
import tkinter as tk
import time

def tirar_dados():
    
    caja1.delete(0,tk.END)
    caja2.delete(0,tk.END)
    
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    time.sleep(1.0)
    caja1.insert(0,dado1)
    caja2.insert(0,dado2)

ventana=tk.Tk()
ventana.title("dados")
ventana.geometry("600x320")
img=tk.PhotoImage(file="img/dadosimg.png")
caja_img=tk.Label(ventana,image=img)

caja_img.pack()



boton=tk.Button(text="Tirar Dados",command=tirar_dados)
boton.place(x=60,y=75)
caja1=tk.Entry()
caja1.place(x=80,y=50,width=20)
caja2=tk.Entry()
caja2.place(x=100,y=50,width=20)
a=caja1
#etiqueta=tk.Label(text="algo" )
#etiqueta.config()
#etiqueta.pack()


ventana.mainloop()