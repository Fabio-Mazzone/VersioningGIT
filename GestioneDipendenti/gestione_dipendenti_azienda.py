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

