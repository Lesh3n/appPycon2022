from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Visualizador:
    def __init__(self,root):
        global lista_imagenes
        
        root.title("Visualizador de fotos")

        self.my_img1 = ImageTk.PhotoImage(Image.open('img/img1.png'))
        self.my_img2 = ImageTk.PhotoImage(Image.open("img/img2.png"))
        self.my_img3 = ImageTk.PhotoImage(Image.open("img/img3.png"))

        lista_imagenes = [self.my_img1, self.my_img2, self.my_img3]

        self.my_label = Label(image=self.my_img1)
        self.my_label.image = self.my_img1
        self.my_label.grid(row=0,column=0,columnspan=3)

        self.btn_atras = Button(root, text="<<", command=lambda:atras(self,0))
        self.btn_sgte = Button(root, text=">>", command=lambda:siguiente(self,2))
        self.btn_salir = Button(root, text="SALIR", command=root.quit())

        self.btn_atras.grid(row=1,column=0)
        self.btn_sgte.grid(row=1,column=2)
        self.btn_salir.grid(row=1,column=1)
    
        def siguiente(self,numero_imagen):
            self.my_label.grid_forget()
            self.my_label = Label(image=lista_imagenes[numero_imagen-1])
            self.my_label.grid(row=0,column=0,columnspan=3)

            self.btn_atras = Button(root, text="<<", command=lambda:atras(self,numero_imagen-1))
            self.btn_sgte = Button(root, text=">>", command=lambda:siguiente(self,numero_imagen+1))

            if numero_imagen == 3:
                self.btn_sgte = Button(root,text=">>", state=DISABLED)

            self.btn_atras.grid(row=1,column=0)
            self.btn_sgte.grid(row=1,column=2)

        def atras(self,numero_imagen):
            self.my_label.grid_forget()
            self.my_label = Label(image=lista_imagenes[numero_imagen-1])
            self.my_label.grid(row=0,column=0,columnspan=3)

            self.btn_atras = Button(root, text="<<", command=lambda:atras(self,numero_imagen-1))
            self.btn_sgte = Button(root, text=">>", command=lambda:siguiente(self,numero_imagen+1))

            if numero_imagen == 1:
                self.btn_atras = Button(root, text="<<", state=DISABLED)

            self.btn_atras.grid(row=1,column=0)
            self.btn_sgte.grid(row=1,column=2)



root = Tk()
Visualizador(root)
root.mainloop()