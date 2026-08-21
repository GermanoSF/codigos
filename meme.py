import string
import time
import os

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
                time.sleep(tempo)
                print(palavra_salva + j)
                os.system('cls')
            if i==j:
                time.sleep(tempo)
                palavra_salva = palavra_salva + j
                print(palavra_salva)
                flag = False

