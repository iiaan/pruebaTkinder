from cgitb import text
import tkinter

expr = ""

def clear():
    global expr
    expr = ""
    eq.set(expr)
    return

def pull(num):
    global expr
    expr = expr + str(num)
    eq.set(expr)
    return

def calc():
    global expr 
    
    tot = str(eval(expr))
    eq.set(tot)
    expr = tot
    
    return


def AddButtons(gui):
    #Primera Fila
    button_clear = tkinter.Button(gui, text="CLEAR", fg= "black", bg="white", command=lambda: clear(), height=2, width=6, borderwidth=0 )
    button_clear.grid(row=1, column=0, padx=5, pady=5)
    
    button_div = tkinter.Button(gui, text=" / ", fg= "black", bg="white", command=lambda: pull("/"), height=2, width=6, borderwidth=0)
    button_div.grid(row=1, column=1, padx=5, pady=5)
    
    button_mult = tkinter.Button(gui, text=" X ", fg= "black", bg="white", command=lambda: pull("*"), height=2, width=6, borderwidth=0)
    button_mult.grid(row=1, column=2, padx=5, pady=5 )
    
    button_plus = tkinter.Button(gui, text=" + ", fg= "black", bg="white", command=lambda: pull("+"), height=2, width=6, borderwidth=0)
    button_plus.grid(row=1, column=3, padx=5, pady=5 )
    

    #Segunda Fila
    
    button_one = tkinter.Button(gui, text=" 1 ", fg= "black", bg="white", command=lambda: pull("1"), height=2, width=6, borderwidth=0)
    button_one.grid(row=2, column=0, padx=5, pady=5)
    
    button_two = tkinter.Button(gui, text=" 2 ", fg= "black", bg="white", command=lambda: pull("2"), height=2, width=6, borderwidth=0)
    button_two.grid(row=2, column=1, padx=5, pady=5)
    
    button_three = tkinter.Button(gui, text=" 3 ", fg= "black", bg="white", command=lambda: pull("3"), height=2, width=6, borderwidth=0)
    button_three.grid(row=2, column=2, padx=5, pady=5)
    
    button_rest = tkinter.Button(gui, text=" - ", fg= "black", bg="white", command=lambda: pull("-"), height=2, width=6, borderwidth=0)
    button_rest.grid(row=2, column=3, padx=5, pady=5)
    #Tercera Fila
    
    button_four = tkinter.Button(gui, text=" 4 ", fg= "black", bg="white", command=lambda: pull("4"), height=2, width=6, borderwidth=0)
    button_four.grid(row=3, column=0, padx=5, pady=5)
    
    button_five = tkinter.Button(gui, text=" 5 ", fg= "black", bg="white", command=lambda: pull("5"), height=2, width=6, borderwidth=0)
    button_five.grid(row=3, column=1, padx=5, pady=5)
    
    button_six = tkinter.Button(gui, text=" 6 ", fg= "black", bg="white", command=lambda: pull("6"), height=2, width=6, borderwidth=0)
    button_six.grid(row=3, column=2, padx=5, pady=5)
    #Cuarta Fila
    
    button_seven = tkinter.Button(gui, text=" 7 ", fg= "black", bg="white", command=lambda: pull("7"), height=2, width=6, borderwidth=0)
    button_seven.grid(row=4, column=0, padx=5, pady=5)
    
    button_eight = tkinter.Button(gui, text=" 8 ", fg= "black", bg="white", command=lambda: pull("8"), height=2, width=6, borderwidth=0)
    button_eight.grid(row=4, column=1, padx=5, pady=5)
    
    button_nine = tkinter.Button(gui, text=" 9 ", fg= "black", bg="white", command=lambda: pull("9"), height=2, width=6, borderwidth=0)
    button_nine.grid(row=4, column=2, padx=5, pady=5)
    
     #Quinta Fila
    
    button_zero = tkinter.Button(gui, text=" 0 ", fg= "black", bg="white", command=lambda: pull("0"), height=2, width=15, borderwidth=0)
    button_zero.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
    
    button_punto = tkinter.Button(gui, text=" . ", fg= "black", bg="white", command=lambda: pull("."), height=2, width=6, borderwidth=0)
    button_punto.grid(row=5, column=2, padx=5, pady=5)
    
    button_igual = tkinter.Button(gui, text=" = ", fg= "black", bg="white", command=lambda: calc(), height=2, width=6, borderwidth=0)
    button_igual.grid(row=5, column=3, padx=5, pady=5)
    
if __name__ == "__main__":
    gui = tkinter.Tk()
    gui.configure(background="gray")
    gui.title("Calculadora")
    gui.iconbitmap("Blackvariant-Shadow135-System-Calculator.ico")
    gui.geometry("242x259")
    
    eq = tkinter.StringVar()
    
    campo_exp = tkinter.Entry(gui, textvariable=eq)
    campo_exp.grid(columnspan=2)
    
    AddButtons(gui)
    
    gui.mainloop()