# GUI = Graphical User Interfaces
import tkinter

window = tkinter.Tk() # classe Tk
window.title("My First GUI Program")
window.minsize(width=500, height=300) # mudando o tamanho da janela

# criando componentes dentro da janela

# classe label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack() # posiciona o label na tela, colocando-o automaticamente no centro caso não haja parâmetro


window.mainloop() # mantém a janela na tela
