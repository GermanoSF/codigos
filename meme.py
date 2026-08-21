import string
import time
import os

def esperar():
    time.sleep(tempo)
    os.system('cls')
    
if __name__ == "__main__":
    lista = list(string.ascii_letters)
    lista.insert(0," ")
    nome = list("Testando terminal")
    tempo = 0.01
    palavra_salva = ""
    flag = bool
    
    for i in nome:
        flag = True
        for j in lista:
            if i != j and flag:
                esperar()
                print(palavra_salva + j)
            if i==j:
                esperar()
                palavra_salva = palavra_salva + j
                print(palavra_salva)
                flag = False

