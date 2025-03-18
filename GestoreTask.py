import shutil
import time
import re
import os
from colorama import Fore, Back, Style

def copia(percorso, nomeFile, percorso_relativo):
    if os.path.exists(percorso):
        indice = 1
        nomeBase, estensione = os.path.splitext(nomeFile)
        nomeCopia = nomeBase + "(" + str(indice) + ")" + estensione
        destinazione = os.path.join(percorso_relativo, nomeCopia)
        while os.path.exists(destinazione):
            indice += 1
            nomeCopia = nomeBase + "(" + str(indice) + ")" + estensione
            destinazione = os.path.join(percorso_relativo, nomeCopia)
        shutil.copy2(percorso, destinazione)
        print(Fore.GREEN + f"{nomeFile} copiato con successo.\n"+ Style.RESET_ALL)
    else:
        print(Fore.RED + "Impossibile copiare, il file non esite.\n" + Style.RESET_ALL)

def rinomina(percorso, percorso_relativo, nomeFile):
    if os.path.exists(percorso):
        nomeNuovo = input(f"Inserisci il nuovo nome del file {nomeFile}.\n")
        file_rinominato = os.path.join(percorso_relativo,nomeNuovo)
        while os.path.exists(file_rinominato):
            print(Fore.LIGHTRED_EX +"Impossibile rinominare più file in modo uguale."+ Style.RESET_ALL)
            nomeNuovo = input("Inserisci un nome diverso da quello inserito prima.\n")
            file_rinominato = os.path.join(percorso_relativo, nomeNuovo)
        os.rename(percorso, file_rinominato)
        print(Fore.GREEN + f"{nomeFile} rinominato con successo in {nomeNuovo}\n"+ Style.RESET_ALL)
    else:
        print(Fore.RED + f"Impossibile rinominare, il file {nomeFile} non esite.\n" + Style.RESET_ALL)

def sovrascrivi(percorso):
    if os.path.exists(percorso):
        print("Inserisci il testo che sovrascriverà il precedente. ")
        testo = input()
        with open(percorso, 'w') as file:
            file.write(str(testo))
            print(Fore.GREEN + "Operazione Eseguita.\n"+ Style.RESET_ALL)
    else:
        print("Inserisci il testo sul file appena creato. ")
        testo = input()
        with open(percorso, 'w') as file:
            file.write(str(testo))
            print(Fore.GREEN + "Operazione Eseguita.\n"+ Style.RESET_ALL)

def aggiungi(percorso, nomeFile):
    print(f"Inserisci il testo da aggiungere in {nomeFile}: ")
    testo = input()
    testo = str(testo)
    with open(percorso, 'a') as file:
        file.write("\n" + testo)
        print(Fore.GREEN + "Operazione Eseguita.\n"+ Style.RESET_ALL)

def elimina(percorso, nomeFile):
    if os.path.exists(percorso):
        os.remove(percorso)
        print(Fore.GREEN + f"{nomeFile} eliminato con successo.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Il file {nomeFile} non esiste.\n" + Style.RESET_ALL)

def leggi(percorso,nomeFile):
    if os.path.exists(percorso):
        with open(percorso, 'r') as file:
            contenuto = file.read()
        if contenuto:
            print(contenuto)
        else:
            print(Fore.RED + f"Impossibile leggere il contenuto, il file {nomeFile} è vuoto.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Impossibile leggere il contenuto, il file {nomeFile} è inesistente.\n" + Style.RESET_ALL)

def cercaTesto(percorso,nomeFile):
    if os.path.exists(percorso):
        testo = input(f"Inserisci il testo da ricercare in {nomeFile}:\n")
        with open(percorso, 'r') as file:
            contenuto = file.read()
        contenutoEvidenziato = ('\n'+re.sub(f'({re.escape(testo)})', Back.LIGHTMAGENTA_EX + Fore.BLACK + r'\1' + Style.RESET_ALL, contenuto)+'\n')
        if testo in contenuto:
            print(contenutoEvidenziato)
        else:
            print(Fore.RED + "Contenuto non trovato.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Impossibile leggere il contenuto, il file è inesistente.\n" + Style.RESET_ALL)

def mostraDimensione(percorso,nomeFile):
    if os.path.exists(percorso):
        dimensione = os.path.getsize(percorso)
        for unita in ['B','KB', 'MB', 'GB', 'TB']:
            if dimensione < 1024:
                print(Fore.LIGHTBLUE_EX +f"la dimensione del file {nomeFile} è: {dimensione:.2f} {unita}."+ Style.RESET_ALL) 
                break
            dimensione /= 1024          
    else:
        print(Fore.RED + f"Il file {nomeFile} non esiste." + Style.RESET_ALL)

def dataModifica(percorso,nomeFile):
    if os.path.exists(percorso):
        timeStamp = os.path.getmtime(percorso)
        modifica = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeStamp))
        print(Fore.LIGHTBLUE_EX + f"L'ultima modifica del file {nomeFile} risale a {modifica}\n"+ Style.RESET_ALL)
    else:
        print(Fore.RED + f"Il file {nomeFile} non esiste." + Style.RESET_ALL)

def dataCreazione(percorso,nomeFile):
    if os.path.exists(percorso):
        timeStamp = os.path.getctime(percorso)
        creazione = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeStamp))
        print(Fore.LIGHTBLUE_EX + f"La creazione del file {nomeFile} risale a {creazione}\n"+ Style.RESET_ALL)
    else:
        print(Fore.RED + f"Il file {nomeFile} non esiste." + Style.RESET_ALL)

def sceltaOperazione():
    while True:
        istruzioni = (
        Back.LIGHTCYAN_EX + Fore.BLACK + "Operazioni Possibili:(Premi il numero corrispondente) " + Style.RESET_ALL + "\n"
        "1. Per scrivere/sovrascrivere.\n"
        "2. Per aggiungere testo.\n"
        "3. Per eliminare il file.\n"
        "4. Per leggere il contenuto.\n"
        "5. Per copiare il file.\n"
        "6. Per rinominare il file.\n"
        "7. Per cercare del contenuto in un file.\n"
        "8. Per controllare la grandezza di un file.\n"
        "9. Per controllare l'ultima modifica di file.\n"
        "10. Per controllare la data di creazione file.\n"
        )
        print(istruzioni)
        scelta = input("Operazione: ")
        if scelta.isdigit():
            scelta = int(scelta)
            if scelta in range(1, 11):
                break
            else:
                print(Fore.RED + "Numero non riconosciuto." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Valore non riconosciuto." + Style.RESET_ALL)
    return scelta

def main():
    while True:
        percorso_relativo = "C:\\Users\\Utente03\\Desktop\\Tasks"
                    
        if not os.path.exists(percorso_relativo):
            print(f"La cartella {percorso_relativo} non esiste, la creo...")
            os.makedirs(percorso_relativo)

        contenuto = os.listdir(percorso_relativo)

        print(Back.LIGHTYELLOW_EX + Fore.BLACK +"Lista dei File:" + Style.RESET_ALL)
        for i, elemento in enumerate(contenuto):
            if i < len(contenuto) - 1:
                print(elemento, end=" | ")
            else:
                print(elemento, end=" ")

        nomeFile = input("\nScegli il file su cui operare, se non c'è verra creato sul momento: ")
        scelta = sceltaOperazione()
        fileMultipli = nomeFile.split()
        for nomeFile in fileMultipli:
            percorso = os.path.join(percorso_relativo, nomeFile)

            match scelta:
                case 1:
                    sovrascrivi(percorso)
                case 2: 
                    aggiungi(percorso,nomeFile)
                case 3: 
                    elimina(percorso,nomeFile)
                case 4: 
                    leggi(percorso,nomeFile)
                case 5: 
                    copia(percorso, nomeFile, percorso_relativo)
                case 6: 
                    rinomina(percorso, percorso_relativo,nomeFile)
                case 7: 
                    cercaTesto(percorso,nomeFile)
                case 8: 
                    mostraDimensione(percorso,nomeFile)
                case 9: 
                    dataModifica(percorso,nomeFile)
                case 10: 
                    dataCreazione(percorso,nomeFile)

main()