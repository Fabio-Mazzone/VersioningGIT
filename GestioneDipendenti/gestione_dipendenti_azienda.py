#sviluppo di un sistema per la gestione dei dipendenti di un azienda.
#il programma deve permettere di:
#1. Inserire un nuovo dipendente con,nome, ID, reparto e stipendio
#2. Visualizzare l'elenco dei dipendenti registrati
#3. modificare le informazioni di un dipendente specifico
#4. calcolare lo stipendio annuale di un dipendente selezionato.



#GestioneDipendenti

#definizione della classe dipendente

class Dipendente:
    def __init__(self, nome, cognome, id_dipendente, reparto, stipendio):   #costruttore della classe dipendente
        self.nome = nome
        self.cognome = cognome                #attributi della classe dipendente  (nome, id_dipendente, reparto, stipendio)
        self.id_dipendente = id_dipendente
        self.reparto = reparto
        self.stipendio = stipendio


    def calcola_stipendio_annuale(self):   #metodo per calcolare lo stipendio annuale
        stipendio_annuale = self.stipendio * 12 #12mesi
        return stipendio_annuale
    
    def modifica_stipendio(self, nuovo_stipendio):  #metodo per modificare lo stipendio
        self.stipendio = nuovo_stipendio
    
    def mostra_info(self):   #metodo per mostrare le informazioni del dipendente
        
        print("Nome: ", self.nome)
        print("cognome: ", self.cognome)
        print("ID: ", self.id_dipendente)
        print("Reparto: ", self.reparto)
        print("Stipendio: ", self.stipendio)
        print("Stipendio annuale: ", self.calcola_stipendio_annuale())
        
#creazione dizionario per gestire i dipendenti, con chiave l'id del dipendente
dipendenti = {}

#funzione per inserire un nuovo dipendente
def aggiungi_dipendente():
    nome = input("Inserisci il nome del dipendente: ")
    cognome = input("Inserisci il cognome del dipendente: ")
    id_dipendente = input("Inserisci l'ID del dipendente: ")
    reparto = input("Inserisci il reparto: ")
    stipendio = float(input("Inserisci lo stipendio: "))
    
    nuovo_dipendente = Dipendente(nome, cognome, id_dipendente, reparto, stipendio)  #creazione di un oggetto di tipo dipendente
    dipendenti[id_dipendente] = nuovo_dipendente
    print("Dipendente aggiunto con successo!")

#funzione per visualizzare l'elenco dei dipendenti
def mostra_tutti_dipendenti():
    if not dipendenti:
        print("Nessun dipendente registrato")    #se il dizionario è vuoto
    else:           #se il dizionario non è vuoto
        for dipendente in dipendenti.values(): # per ogni dipendente nel dizionario dei dipendenti1
            dipendente.mostra_info()         # mostra le informazioni del dipendente
        print("------------------------")


#funzione per modificare le informazioni di un dipendente
def modifica_dipendente():              #funzione per modificare le informazioni di un dipendente
    id_dipendente = input("Inserisci l'ID del dipendente da modificare: ")   #chiede l'id del dipendente da modificare 
    if id_dipendente in dipendenti:                     #se l'id del dipendente è presente nel dizionario dei dipendenti
        print("1. Modificare Nome")                #chiede cosa si vuole modificare 
        print("2. Modificare Cognome")
        print("3. Modificare Reparto")            
        print("4. Modificare Stipendio")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            nuovo_nome = input("Inserisci il nuovo nome: ")
            dipendenti[id_dipendente].nome = nuovo_nome #modifica il nome del dipendente con il nuovo nome #.nome è l'attributo della classe dipendente
        elif scelta == "2":
            nuovo_cognome = input("Inserisci il nuovo cognome: ")
            dipendenti[id_dipendente].cognome = nuovo_cognome
        elif scelta == "3":
            nuovo_reparto = input("Inserisci il nuovo reparto: ")
            dipendenti[id_dipendente].reparto = nuovo_reparto
        elif scelta == "4":
            nuovo_stipendio = float(input("Inserisci il nuovo stipendio: "))
            dipendenti[id_dipendente].modifica_stipendio(nuovo_stipendio)
        


        else:
            print("Scelta non valida.")
        
        print("Modifica effettuata con successo!")
    else:
        print("Dipendente non trovato.")



while True:   #ciclo infinito
    print("1. Aggiungi dipendente")  #menu
    print("2. Mostra tutti i dipendenti")
    print("3. Modifica dipendente")
    
    print("4. Esci")    
    
    scelta = input("Scegli un'opzione: ")  #chiede all'utente di scegliere un'opzione
    
    if scelta == "1":  #se l'utente sceglie 1
        aggiungi_dipendente()  #richiama la funzione aggiungi_dipendente
    elif scelta == "2":  #se l'utente sceglie 2
        mostra_tutti_dipendenti()  #richiama la funzione mostra_tutti_dipendenti
    elif scelta == "3":  #se l'utente sceglie 3
        modifica_dipendente()  #richiama la funzione modifica_dipendente
    
    elif scelta == "4":
        break #se l'utente sceglie 5 esce dal ciclo