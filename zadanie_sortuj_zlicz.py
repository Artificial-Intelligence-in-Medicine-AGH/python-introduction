def sortuj(t):
    n = len(t)
    if n <=1: return t
    # selection sort O(n**2)
    for i in range(0,n-1):
        nm = i
        for j in range(i+1,n):
            if t[j] < t[nm]: nm = j
        t[nm], t[i] = t[i], t[nm]
    return t

def zlicz(t):
    cnt = 0
    for i in range(len(t)):
        cnt += 1
    return cnt

t = [1,14,2,5,9,7]
print("Elementów: {}".format(zlicz(t)))
sortuj(t)
print("Posortowana lista:")
for el in t: print(el, end=" ") 