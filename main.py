import numpy as np
#import matplotlib

def sort(lista, dlugosc):
    for i in range(dlugosc - 1):
        for j in range(dlugosc - i - 1):
            if(lista[j] > lista[j + 1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

    
    return lista;    

def main():
    lista = np.random.randint(0, 6, 20).tolist()

    #for i in lista:
    #    print(i)

    posortowanaLista = sort(lista, 20)

    #print("sortowanie") debug

    #for i in lista:
    #    print(i)    
        
    temp = 0
    
    for i in range(0, 6):
        for l in lista:
            if(l == i):
                temp += 1
        print(f"\"{i}\" - {temp}")
        temp = 0
        

if __name__ == "__main__":
    main()
