lista = []
print("Lunghezza lista")
n = int(input())
s = 0
for elem in range(0,n):
    print("elemento ", elem+1)
    lista.append(int(input()))
for elem in lista:
    s = s + elem
print("la somma e' : ", s)