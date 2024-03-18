from tkinter import Tk, filedialog, Button, messagebox, Entry, Text, END, CENTER, Label, LEFT, RIGHT, Frame, BOTTOM, TOP

class Window:
    def __init__(self, title, geometry):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(geometry)

        #Main frame
        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        #Window title
        self.window_title = Label(self.main_frame, text=title, font=("Arial", 14, "bold"))
        self.window_title.pack(pady=10)


    # Mostrar Janela
    def showWindow(self):
        self.window.mainloop()

    #Adicionar botão a janela
    def addButton(self, texto: str, comando, **kwargs: dict):
        button = Button(self.main_frame, text=texto, command=comando, **kwargs)
        button.pack(side=LEFT, padx=10)

    #Adiciona titulo a janela
    def addTitle(self, texto: str, **kwargs):
        label = Label(self.main_frame, text=texto, **kwargs)
        label.pack(side=LEFT, padx=10)

    #Adiciona entrada de texto
    def textEntry(self, **kwargs):
        text_entry = Entry(self.main_frame, **kwargs)
        text_entry.pack(side=LEFT, padx=10)


    #Adiciona area de texto
    def textArea(self, **kwargs):
        text_area = Text(self.main_frame, **kwargs)
        text_area.pack(side=LEFT, padx=10)
    #Mostrar Mensagem
    def showMessage(self,type, title, message):
        if type == "info":
            messagebox.showinfo(title,message)
        elif type == "error":
            messagebox.showerror(title, message)

