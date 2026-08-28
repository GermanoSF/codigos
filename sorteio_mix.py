import random

nomes = ['XGG','Nadaol','Claudio','Novaez']
tamanho_nomes = 7

def funct(indice):
    for i in range(tamanho_nomes):
            if len(nomes[indice])>i:
                print(f"{nomes[indice][i]}", end="")
            else:
                print(' ',end="")
    nomes.pop(indice)

if __name__ == "__main__":

    while len(nomes)>1:

        funct(random.randrange(len(nomes)))
        print(' ||| ', end="")

        funct(random.randrange(len(nomes)))
        print()
