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

