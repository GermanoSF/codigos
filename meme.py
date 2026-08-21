import string
import time
import os

if __name__ == "__main__":
    lista = []
    lista.append(' ')
    lista.append(list(string.ascii_letters))
    nome = list("Leonardo dos hs")
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
                print(palavra_salva + j)
                palavra_salva = palavra_salva + j
                flag = False

