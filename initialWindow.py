from tkinter import Tk, filedialog, Button, messagebox, Entry, Text, END, CENTER, Label, LEFT, RIGHT, Frame, BOTTOM, TOP
from baseWindow import Window

class initialWindow(Window):
    def __init__(self):
        super().__init__("Bem vindo", '300x150')
        # self.title = "Janela Inicial"

        # Titulo
        self.rotulo = Label(self.main_frame, text='Bem vindo ao nosso Software de Clusterização, deseja prosseguir ou sair do programa?', wraplength=300)
        self.rotulo.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Frame para botões
        self.frame_button = Frame(self.main_frame)
        self.frame_button.pack(side=BOTTOM, pady=15)
        # Botão sair
        self.button_leave = Button(self.frame_button, text='Sair', bg="red", fg="white", command=self.sair)
        self.button_leave.pack(side=LEFT, padx=10)
        # Botão prosseguir
        self.button_go = Button(self.frame_button, text="Iniciar IA",  bg="blue", fg="white", command=self.prosseguir)
        self.button_go.pack(side=LEFT, padx=10)


    def prosseguir(self):
        print("Indo pro programa...")  # Placeholder example
        self.window.destroy()  # Closes the main window
    def sair(self):
            print("Saindo do programa...")  # Placeholder example
            self.window.destroy()  # Closes the main window


# # Inicializando janela
# janelaInicial = initialWindow()
# janelaInicial.showWindow()