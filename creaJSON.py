import os
import json

os.system("clear")
print("PARTE 1 · DATI DEL SET")
input("Premere INVIO per continuare...")
os.system("clear")

#NOME SET
nomeSet = input("Inserire il nome del set: ")
while (nomeSet.isalnum() and not nomeSet.isalpha()) or nomeSet.isnumeric() or nomeSet.isspace():
	nomeSet = input("ERRORE! Inserire il nome del set: ")

#NUMERO SET
numSet = input("Inserire il numero del set: ")
while not numSet.isnumeric() or int(numSet) < 0 or int(numSet) > 88:
		numSet = input("ERRORE! Inserire il numero del set: ")

#ANNO SET
annoSet = input("Inserire l'anno di uscita del set: ")
while not annoSet.isnumeric() or int(annoSet) < 2000 or int(annoSet) > 2023:
		annoSet = input("ERRORE! Inserire l'anno di uscita del set: ")

os.system("clear")
print("PARTE 2 · DATI FIGURINE")
input("Premere INVIO per continuare...")
os.system("clear")

listaFigurine = []

while True:
    #NOME CARTA
    nomeCarta = input("Inserire il nome della carta (o digitare 'FINE' per terminare l'inserimento): ")
    while (nomeCarta.isalnum() and not nomeCarta.isalpha()) or nomeCarta.isnumeric() or nomeCarta.isspace():
        nomeCarta = input("ERRORE! Inserire il nome della carta (o digitare 'FINE' per terminare l'inserimento): ")

    #CONTROLLO SE L'UTENTE HA SCELTO DI USCIRE
    if nomeCarta == "FINE" or nomeCarta == "fine" or nomeCarta == "Fine":
        break

	#NUMERO CARTA
    numCarta = input("Inserire il numero della carta: ")
    while not numCarta.isnumeric() or int(numCarta) < 0:
        numCarta = input("ERRORE! Inserire il numero della carta: ")

    #URL IMMAGINE
    urlCarta = input("Incollare l'url della foto della carta (SHIFT + CTRL + V): ")
    while urlCarta.isspace() or urlCarta == "\n":
        urlCarta = input("ERRORE! Incollare l'url della foto della carta (SHIFT + CTRL + V): ")
    
    #TIPO CARTA
    listaTipoCarta = []
    #1 è obbligatorio
    tipoCarta = input("Inserire il tipo della carta: ")
    while (tipoCarta.isalnum() and not tipoCarta.isalpha()) or tipoCarta.isnumeric() or tipoCarta.isspace():
        tipoCarta = input("ERRORE! Inserire il tipo della carta: ")
    listaTipoCarta.append(tipoCarta.capitalize())
    #eventuali aggiuntivi
    while True:
        tipoCarta = input("Inserire un eventuale secondo tipo della carta (o digitare 'FINE' per terminare l'inserimento): ")
        while (tipoCarta.isalnum() and not tipoCarta.isalpha()) or tipoCarta.isnumeric() or tipoCarta.isspace():
            tipoCarta = input("ERRORE! Inserire un eventuale secondo tipo della carta (o digitare 'FINE' per terminare l'inserimento): ")
        #Controllo se l'utente ha deciso di uscire
        if tipoCarta == "FINE" or tipoCarta == "fine" or tipoCarta == "Fine":
            break
        listaTipoCarta.append(tipoCarta.capitalize())

    #PUNTI SALUTE
    puntiSalute = input("Inserire i punti salute (PS) della carta: ")
    while not puntiSalute.isnumeric() or int(puntiSalute) < 0:
        puntiSalute = input("ERRORE! Inserire i punti salute (PS) della carta: ")

    #SALVO I DATI DELLA CARTA IN UNA STRUTTURA JSON
    carta = {
        'numero': numCarta,
        'nome': nomeCarta.capitalize(),
        'url': urlCarta.lower(),
        'tipo': listaTipoCarta,
        'PS': puntiSalute
    }

    #AGGIUNGO LA CARTA APPENA MEMORIZZATA ALLA LISTA DELLE FIGURINE
    listaFigurine.append(carta)
    print("\n")

#SALVO I DATI DEL SET IN UNA STRUTTURA JSON
data = {
    'numeroSet': numSet,
    'nomeSet': nomeSet.capitalize(),
    'anno di uscita': annoSet,
    'figurine': listaFigurine
}

#SCRIVO SUL FILE JSON
with open("output.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

os.system("clear")
print("IL TUO FILE JSON È STATO CREATO!")