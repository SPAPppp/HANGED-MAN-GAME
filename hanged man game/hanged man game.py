import random
from tkinter import *
from tkinter import ttk
import copy

words = [["c","a","m","e","l"],["c","e","s","a","r"],["c","e","l","l","f","o","n","e"],["t","u","r","t","l","e"],["r","o","m","o","l","o"]]
hint = [["animal, brand of cigarette"],["he said \"I come, I saw, I won\""],["use it to call"],["a tortoise that goes very slowly"],["first king of Rome"]]

root=Tk()
root.title("test hanged man GUI")
root.geometry("500x600+500+75")
root.resizable(False,False)



img0 = PhotoImage(file="hanged img0.png")
img1 = PhotoImage(file="hanged img1.png")
img2 = PhotoImage(file="hanged img2.png")
img3 = PhotoImage(file="hanged img3.png")
img4 = PhotoImage(file="hanged img4.png")
img5 = PhotoImage(file="hanged img5.png")
img6 = PhotoImage(file="hanged img6.png")
lb=ttk.Label(root, image=img0); lb.pack()

errors = 0

w = random.randint(0, ( len(words) - 1))

cw = copy.copy(words[w])         #la parola corretta

def cacancel_caracter (w) :
    i=1
    while i<=(len(w)/2):
        x = random.randint(0, (len(w) - 1))
        if w[x] == int: i = i 
        else :
            w[x] = x+1
            i += 1
    return w


hint_lbl= ttk.Label(root, text=hint[w], background="orange", font=(24)); hint_lbl.pack(fill=X, padx=10)
ww = cacancel_caracter(words[w])
 
def verify_index() :
    index = STRINGVARindex.get() 
    try:
        if int(index) > int(len(ww)) : 
            q1.config(text="ERROR")
            q1.after(1500, lambda: q1.config(text="which red-marked position do you want to replace with a letter?"))
    except ValueError:
        q1.config(text="ERROR")
        q1.after(2000, lambda: q1.config(text="which red-marked position do you want to replace with a letter?"))
    else: 
        e1.config(foreground="green")
        e1.after(500, lambda: e1.config(foreground="black"))

def verify_letter():
    index = STRINGVARindex.get() 
    letter = STRINGVARletter.get()
    if letter == cw[int(index)-1] :
        ww[int(index)-1] = letter
        clear_frame()
        voice_word(ww)
        e1.delete(0, END)
        e2.delete(0, END)
    else:
        global errors
        errors+=1
        e2.delete(0, END)
        voice_immagine()



phrase=Frame(root, width=500, height=200, background="blue")
phrase.pack(fill=X, pady=10)

def voice_immagine():
    if errors == 0: lb.config(image=img0)
    elif errors == 1: lb.config(image=img1)
    elif errors == 2: lb.config(image=img2)
    elif errors == 3: lb.config(image=img3) 
    elif errors == 4: lb.config(image=img4)
    elif errors == 5: lb.config(image=img5)
    elif errors == 6: lb.config(image=img6)

def voice_word(ww):        #funzione che fa visualizzare la parola 
    for letters in ww:
        try:
            int(letters)
            Label(phrase, text=letters, font=(4), padx=20, foreground="red").pack(fill=BOTH, expand=True, side=LEFT)
        except ValueError:    
            Label(phrase, text=letters, font=(24), padx=20).pack(fill=BOTH, expand=True, side=LEFT)
    voice_word

voice_word(ww)

def clear_frame():
   for widgets in phrase.winfo_children():
      widgets.destroy()

fq1= Frame(root, width=500, height=200, background="red")   #frame question one
fq1.pack(padx=5, pady=10)
q1= Label(fq1, text="which red-marked position do you want to replace with a letter?", font=("Helvetica",10))
q1.pack(fill=BOTH, expand=True, side=LEFT)
STRINGVARindex=StringVar()
e1= ttk.Entry(fq1, textvariable=STRINGVARindex, width=7, font=("Helvetica",10))
e1.pack(fill=BOTH, expand=True, side=LEFT)
e1.bind("<Return>", lambda e: verify_index())
b1= ttk.Button(fq1, text="select", command=verify_index, default = 'active')
b1.pack(fill=BOTH, expand=True, side=LEFT)

fq2= Frame(root, width=500, height=200, background="red")   #frame question two
fq2.pack(padx=5, pady=10)
q2= Label(fq2, text="Which letter do you want replace in the position?", font=("Helvetica",10))
q2.pack(fill=BOTH, expand=True, side=LEFT)
STRINGVARletter=StringVar()
e2=Entry(fq2, textvariable=STRINGVARletter, width=7)
e2.bind("<Return>", lambda e: verify_letter())
e2.pack(fill=BOTH, expand=True, side=LEFT)
b2= ttk.Button(fq2, text="select", command= verify_letter)
b2.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()