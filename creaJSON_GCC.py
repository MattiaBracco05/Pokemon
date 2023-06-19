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

#TOT FIGURINE SET
figurineTotSet = input("Inserire il numero di figurine totali nel set: ")
while not figurineTotSet.isnumeric() or int(figurineTotSet) < 0 or int(figurineTotSet) > 500:
		figurineTotSet = input("ERRORE! Inserire il numero di figurine totali nel set: ")

os.system("clear")
print("PARTE 2 · DATI FIGURINE")
input("Premere INVIO per continuare...")
os.system("clear")

listaFigurine = []
i = 1

while True:
    #NOME CARTA
    nomeCarta = input("Inserire il nome della carta (o digitare 'FINE' per terminare l'inserimento): ")
    while (nomeCarta.isalnum() and not nomeCarta.isalpha()) or nomeCarta.isnumeric() or nomeCarta.isspace():
        nomeCarta = input("ERRORE! Inserire il nome della carta (o digitare 'FINE' per terminare l'inserimento): ")

    #CONTROLLO SE L'UTENTE HA SCELTO DI USCIRE
    if nomeCarta == "FINE" or nomeCarta == "fine" or nomeCarta == "Fine":
        break

		#NUMERO CARTA NEL SET (assegnato automaticamente)
    numCarta = i
    print("Numero della carta nel set assegnato automaticamente...")
    
    #NUMERO CARTA (seriale)
    numCartaSeriale = input("Inserire il numero seriale della carta: ")
    while not numCartaSeriale.isalnum() or int(numCartaSeriale) < 1 or int(numCartaSeriale) > 2000:
    	numCartaSeriale = input("Inserire il numero seriale della carta: ")
    
    #URL IMMAGINE
    urlCarta = input("Incollare l'url della foto della carta (SHIFT + CTRL + V): ")
    while urlCarta.isspace() or urlCarta == "\n":
        urlCarta = input("ERRORE! Incollare l'url della foto della carta (SHIFT + CTRL + V): ")
    
    #STADIO EVOLUTIVO
    stadio = input("Inserire lo stadio evolutivo [1-4] (1 = base, 4 = max): ")
    while not stadio.isalnum() or int(stadio) < 1 or int(stadio) > 4:
    	stadio = input("Inserire lo stadio evolutivo (1-4): ")
    #Converto in intero dopo il controllo
    stadio = int(stadio)
    #Assegno il valore
    stadioEvolutivo = ""
    if stadio == 1:
    	stadioEvolutivo = "Base"
    if stadio == 2:
    	stadioEvolutivo = "Fase 1"
    if stadio == 3:
    	stadioEvolutivo = "Fase 2"
    if stadio == 4:
    	stadioEvolutivo = "Fase 3"   
    
    #ABILITÀ CARTA
    listaAbilitaCarta = []
    #1 è obbligatorio
    abilitaCarta = input("Inserire l'abilità della carta: ")
    while (abilitaCarta.isalnum() and not abilitaCarta.isalpha()) or abilitaCarta.isnumeric() or abilitaCarta.isspace():
        abilitaCarta = input("ERRORE! Inserire l'abilità della carta: ")
    listaAbilitaCarta.append(abilitaCarta.capitalize())
    #eventuali aggiuntivi
    while True:
        abilitaCarta = input("Inserire un eventuale secondo tipo di abilità (o digitare 'FINE' per terminare l'inserimento): ")
        while (abilitaCarta.isalnum() and not abilitaCarta.isalpha()) or abilitaCarta.isnumeric() or abilitaCarta.isspace():
            abilitaCarta = input("ERRORE! Inserire un eventuale secondo tipo di abilità (o digitare 'FINE' per terminare l'inserimento): ")
        #Controllo se l'utente ha deciso di uscire
        if abilitaCarta == "FINE" or abilitaCarta == "fine" or abilitaCarta == "Fine":
            break
        listaAbilitaCarta.append(abilitaCarta.capitalize())

    #MOSSE CARTA
    listaMosseCarta = []
    #1 è obbligatorio
    mossaCarta = input("Inserire la mossa della carta: ")
    while (mossaCarta.isalnum() and not mossaCarta.isalpha()) or mossaCarta.isnumeric() or mossaCarta.isspace():
        mossaCarta = input("ERRORE! Inserire la mossa della carta: ")
    listaMosseCarta.append(mossaCarta.capitalize())
    #eventuali aggiuntivi
    while True:
        mossaCarta = input("Inserire un eventuale mossa aggiuntiva (o digitare 'FINE' per terminare l'inserimento): ")
        while (mossaCarta.isalnum() and not mossaCarta.isalpha()) or mossaCarta.isnumeric() or mossaCarta.isspace():
            mossaCarta = input("ERRORE! Inserire un eventuale mossa aggiuntiva (o digitare 'FINE' per terminare l'inserimento): ")
        #Controllo se l'utente ha deciso di uscire
        if mossaCarta == "FINE" or mossaCarta == "fine" or mossaCarta == "Fine":
            break
        listaMosseCarta.append(mossaCarta.capitalize())


    #SALVO I DATI DELLA CARTA IN UNA STRUTTURA JSON
    carta = {
        'numero': str(numCarta) + "/" + figurineTotSet,
        'numeroSeriale': numCartaSeriale,
        'nome': nomeCarta.capitalize(),
        'url': urlCarta.lower(),
        'stadio': stadioEvolutivo,
        'abilita': listaAbilitaCarta,
        'mosse': listaMosseCarta
    }

    #AGGIUNGO LA CARTA APPENA MEMORIZZATA ALLA LISTA DELLE FIGURINE
    listaFigurine.append(carta)
    print("\n")
    
    #INCRMENTO IL NUMERO DELLA CARTA
    i+=1

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
