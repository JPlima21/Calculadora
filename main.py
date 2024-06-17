from tkinter import * # type: ignore
from tkinter import ttk

cor0 = '#232423'
cor1 = '#0a0a0a' #preta
cor2 = '#f2f0f0' #branco
cor3 = '#04375c' #azul
cor4 = '#ECEFF1' #cinza
cor5 = '#fcb103' #laranja

window = Tk()
window.title('Calculator')
window.geometry('320x430')
window.config(bg=cor1)
window.resizable(width=False, height=False)

#Make Frames
frame_screem = Frame(window, width=335, height=60, bg=cor0)
frame_screem.grid(row=0, column=0)

frame_body = Frame(window, width=335, height=388, )
frame_body.grid(row=1, column=0)

#Creating function
all_values = '' 

def entrada_valores(e):
    global all_values
   
    if e in ('+', '-', '*', '/', '%', '.'):
        if  all_values[-1] in ('+', '-', '*', '/', '%', '.'):
            all_values = all_values.strip(all_values[-1]) + str(e)
        else:
            all_values += str(e)       
    else:
        all_values += str(e)

    #Pass the value to screem
    value_text.set(all_values)

#function for calculate
def calculate():
    global all_values

    result = eval(all_values)
    all_values = ''
    all_values = all_values + str(result)
    value_text.set(str(result))

#function clear screem
def clear_screem():
    global all_values

    all_values = ''
    value_text.set('')


#Make a label
value_text = StringVar()

app_label = Label(frame_screem, textvariable=value_text, width=18, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 20 bold'), bg=cor0, fg=cor2)
app_label.place(x=0,y=0)

#Make buttons
b_clear = Button(frame_body, command=clear_screem, text='C', width=11, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=-4, y=0)

b_porcent = Button(frame_body, command = lambda: entrada_valores('%'), text='%', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_porcent.place(x=160, y=0)


#Botões de lateral direita
b_divisao = Button(frame_body, command = lambda: entrada_valores('/'), text='÷', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=240, y=0)

b_multiplicacao = Button(frame_body, command = lambda: entrada_valores('*'), text='x', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_multiplicacao.place(x=240, y=74)

b_subitracao = Button(frame_body, command = lambda: entrada_valores('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_subitracao.place(x=240, y=148)

b_adição = Button(frame_body, command = lambda: entrada_valores('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_adição.place(x=240, y=222)

b_igual = Button(frame_body, command = lambda: calculate(), text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=240, y=296)

b_0= Button(frame_body, command = lambda: entrada_valores('.'), text='.', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=160, y=296)

#Botões númericos
b_0= Button(frame_body, command = lambda: entrada_valores('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=-4, y=296)

b_1= Button(frame_body, command = lambda: entrada_valores('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=222)

b_2= Button(frame_body, command = lambda: entrada_valores('2'), text='2', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=80, y=222)

b_3= Button(frame_body, command = lambda: entrada_valores('3'), text='3', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=160, y=222)

b_4= Button(frame_body, command = lambda: entrada_valores('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=148)

b_5= Button(frame_body, command = lambda: entrada_valores('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=148)

b_6= Button(frame_body, command = lambda: entrada_valores('6'), text='6', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=148)

b_7= Button(frame_body, command = lambda: entrada_valores('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=74)

b_8= Button(frame_body, command = lambda: entrada_valores('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=80, y=74)

b_9= Button(frame_body, command = lambda: entrada_valores('9'), text='9', width=5, height=2, bg=cor4, font=('Ivy 17 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=160, y=74)




window.mainloop()