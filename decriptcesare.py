import string
import random

def decifra_cesare():
    messaggio=input("Inserisci il messaggio da decifrare: ")
    conosce_chiave=input("\nConosci la chiave?\n[1]Si\n[0]No\n")
    def decifra_carattere(c,chiave):
        if c.isalpha():
            risultato=ord('A') if c.isupper() else ord('a')
            return chr((ord(c)-risultato-chiave)%26+risultato)
        return c
    if conosce_chiave=="1":
        chiave=int(input("Inserisci la chiave(1-25): "))
        messaggio_decifrato=''.join(decifra_carattere(c,chiave)for c in messaggio)
        print(f"Messaggio decifrato: {messaggio_decifrato}") 
    elif conosce_chiave=="0":
        print("Provo tutte le combinazioni:")
        for chiave in range(1,26):
            messaggio_decifrato=''.join(decifra_carattere(c,chiave) for c in messaggio)
            print(f"Chiave {chiave}: {messaggio_decifrato}")
    else:
        print("Input non valido, riprova.")

def cifra_cesare():
    messaggio=input("Inserisci il messaggio da cifrare: ")
    chiave=random.randint(1,25)
    def cifra_carattere(c,chiave):
        if c.isalpha():
            risultato=ord('A') if c.isupper() else ord('a')
            return chr((ord(c)-risultato+chiave)%26+risultato)
        return c
    messaggio_cifrato=''.join(cifra_carattere(c,chiave) for c in messaggio)
    print(f"Messaggio cifrato: {messaggio_cifrato}\n chiave={chiave}")
    
print("*********************\nCrypt/Encrypt Cesare\n*********************\n")

while True:
    print("Cosa vuoi fare? ")
    comando=input("[1]Crypt\n[2]Encrypt\n[0]EXIT\n")
    if comando=="0":
        break
    elif comando=="1":
        cifra_cesare()
    elif comando=="2":
        decifra_cesare()
    else:
        print("Input errato")