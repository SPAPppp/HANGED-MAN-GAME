import random
import copy

words = [["c","a","m","m","e","l","o"],["c","e","s","a","r","e"],["t","e","l","e","f","o","n","o"],["t","a","r","t","a","r","u","g","a"],["r","o","m","o","l","o"]]
hint = [["ha due gobbe piene di grasso"],["colui che disse \"veni, vidi, vinci\""],["lo usi per chimare"],["una testuggine che va molto piano"],["il primo re di Roma"]]
# creazione della classe dell'impiccato
class hanged_man : 
    def __init__(self, head, body, arm, leg):
        self.head = head
        self.body = body
        self.arm = arm
        self.leg = leg

# si crea l'istanza dell'impiccato
stickman = hanged_man(False,False,0,0)

# mattiamo la variazione dell'istanza che avrà se il giocatore comette un errore 
def error_variation (stickman, x) :
    if x == 1 : stickman = hanged_man(True,False,0,0)
    elif x == 2 : stickman = hanged_man(True,True,0,0)
    elif x == 3 : stickman = hanged_man(True,True,1,0)
    elif x == 4 : stickman = hanged_man(True,True,2,0)
    elif x == 5 : stickman = hanged_man(True,True,2,1)
    elif x == 6 : stickman = hanged_man(True,True,2,2)
    return stickman

# creiamo l'ultimo tipo di istanza accettabile dal prugramma 
death_stickman = hanged_man(True,True,2,2)

# piccolo dettaglio da perfeionista, se ha piu di una gamba o braccia, 
# anzi che fare tanti print(... utilizzo direttamnte questa funzione
def describe_stickman (head, body, arm, leg) :
    x = "arm"
    if(stickman.arm > 1) :
        x = "arms"
    y = "leg"
    if(stickman.leg > 1) :
        y = "legs"
    print(f"head:{head}\nbody:{body}\n{x}:{arm}\n{y}:{leg}")

# funzione gia pronta da utilizzare per quando mi serve
# describe_stickman (stickman.head, stickman.body,stickman.arm, stickman.leg)

# estraimo casualemte una parola

w = random.randint(0, ( len(words) - 1))
hint_wanted_word = hint[w]
correct_wanted_word = copy.copy(words[w])
# funzione che elimina i caratteri della parola, che poi il giocatore dovrà indovinare
def cancel_caracter (wanted_word) :
    w = 0
    while w < (len(wanted_word) - (len(wanted_word) / 2)) :
        x = random.randint(0, (len(wanted_word) - 1))
        if wanted_word[x] == "_" : w -= 1 
        else : wanted_word[x] = "_"
        w += 1
    return wanted_word

wanted_word = cancel_caracter(words[w])

# scrive gli indici della parola in modo che il giocatore possa sapere con qule numero sono indiczzate le parole 
def get_indices (wanted_word) :
    indices = []
    for x in range(len(wanted_word)) : indices.append(x)
    w = 0 
    while w < len(wanted_word) : 
        indices[w] = str(indices[w])
        w += 1
    return indices

indices = get_indices(wanted_word)

# l'interfaccia che si mostrera al giocatore 
print("questo è il gioco dell'impiccato,")
def question_1 (x) :
    print(f"indovina la parola: {x}")
    print(f"                    {indices}")
    print (hint[w])
    print(describe_stickman (stickman.head, stickman.body,stickman.arm, stickman.leg))
    index = input("dimmi l'indice in cui vuoi inserie la lettera ")
    return index

# se il giocatore azzeccherà la lettera della wanted_word cambierà, 
# altrimenti la variabile stick aumenterà e farà variare l'istanza dell'impiccato
def question_2 (ind) : 
    stick = 0
    l = input(f"che lettera vuoi mettere nella casella {int(ind)} ")
    if l == correct_wanted_word[int(ind)] : 
        wanted_word[int(ind)] = l 
        return wanted_word
    else : stick += 1
    return stick
# diamo via al ciclo di gioco che terminera o con il completamento dell'impiccato,
# o con il completamento della parola 
index = question_1(wanted_word)
stick = 0
v = 0
while v == 0:
    if int(index) > len(wanted_word) :                      # se l'indice è piu lungo della wanted_word 
        print("ERROR\n indice troppo grande")               # rimetti un'altro indice  
        index = question_1(wanted_word)
    if wanted_word[int(index)] != "_" :                     # se l'indice che hai messo contiene una lettera 
        print("ERROR\n hai gia questa lettera")             # rimetti un'altro indice 
        index = question_1(wanted_word)
    else :
        letter = question_2(index)                          # metti una lettera, se questa corrisponde a quella nella correct_wanted_word vai avanti 
        if type(letter) == int :                            # altrimenti incrementerai un valore il quale fara variare le caratteristiche dell'istanza dello stickman
            print("LETTERA SBAGLIATA")
            stick += 1 
            stickman = error_variation(stickman, stick)
            index = 0
    if stick == 6 :                                         # se hai finito i tentativi
        print("YOU LOSE")                                   # hai perso il gioco 
        break 
    elif wanted_word == correct_wanted_word :               # se hai completato la parola 
        print("YOU WIN")                                    # vinci il gioco 
        break
    index = question_1(wanted_word)                         # richiedi l'indice in cui vuoi far inserire la lettere e fai ripetere il ciclo 
