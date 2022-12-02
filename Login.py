from tkinter import *
from tkinter import messagebox

credenciales = {
    'user':'prueba',
    'pass':'123'
}

def validacion(self):
        #Se obtienen los datos de las entryBoxes
        usuario = self.usuario.get()
        password = self.password.get()
        if credenciales['user'] != usuario and credenciales['pass'] == password:
            messagebox.showerror(message='Usuario y password incorrectas.')
        else:
            messagebox.showinfo(message="Dirigiendose a visualizador de fotos.")
            root.destroy()
            invocar_fotos()

def invocar_fotos():
    import Visualizador


class Login:
    def __init__(self,root):
        root.title("Login")
        
        titulo = Label(text="Bienvenido!", font=("Times New Roman",20,"italic"), justify=CENTER)
        titulo.place(x=50,y=40)

        self.usuario = StringVar()
        label_usuario = Label(text="Usuario").place(x=60,y=95)
        input_usuario = Entry(root,width=25,justify="center",textvariable=self.usuario).place(x=42,y=125)


        self.password = StringVar()
        label_password = Label(text="Contrasena").place(x=80,y=180)
        input_contra = Entry(root, width=25, show='*', justify="center", textvariable=self.password).place(x=40,y=210)

        boton = Button(root, text="Iniciar Sesion", bg="green", pady=10, padx=6, command=lambda:validacion(self)).place(x=55,y=260)


root = Tk()
root.geometry("240x400")
Login(root)
root.mainloop()

        

