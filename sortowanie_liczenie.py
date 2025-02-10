import random

#tworzenie listy
lista_1 = []
for i in range (20):
    lista_1.append(random.randint(0,5))

print(lista_1)

#sortowanie listy - insertion sort
def sortuj(elements):
    for i in range(1, len(elements)):
        j = i - 1
        next_element = elements[i]

        while j >=0 and elements[j] > next_element:
            elements[j+1] = elements[j]
            j -= 1

        elements[j + 1] = next_element
    return elements

sortuj(lista_1)
print(lista_1)


#zliczanie ilości wystąpień danego elementu w liście
def policz(liczba: int, lista: list) -> int:
    return lista.count(liczba)

print("Ilość wystąpień poszczególnych liczb:")
i = 0
while i <= 5:
    ilosc = policz(i, lista_1)
    print(f"\"{i}\" - {ilosc}")
    i += 1
