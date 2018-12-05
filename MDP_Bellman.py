"""
s - stan,
a - akcja, którą można wykonać w danym stanie,
R(s) - koszt bycia w stanie s,
T(s, a, s') = P(s'|s, a) - prawdopodobieństwo przejścia w stan s' ze stanu s, przy wybraniu akcji a.
"""
from copy import deepcopy
from math import fabs
from obliczenia import wybierzNajlepszaAkcje

R = []
typPola = []
rozmiar = []
plik = open("siatka.txt", mode="r")
for i, linia in enumerate(plik.readlines()):
    if i == 0:
        rozmiar = [int(x) for x in linia.split()]
    if i <= rozmiar[1] and i >0:
        typPola.append([float(x) for x in linia.split()])
    if i > rozmiar[1]+1:
        R.append([float(x) for x in linia.split()])
plik.close()
testDoZakonczenia = []
#print(rozmiar)
#print(R)
#print(typPola)
V = deepcopy(R)
y = 0.5
politykaRuchu=[]
for i in range(100):
    stareV = V

    noweParamatery = wybierzNajlepszaAkcje(rozmiar, typPola, V, R, y)
    V = deepcopy(noweParamatery[1])
    politykaRuchu = deepcopy(noweParamatery[0])

    #print(noweParamatery)
    for wiersz in range(rozmiar[1]):
        for kolumna in range(rozmiar[0]):
            testDoZakonczenia.append(fabs(stareV[wiersz][kolumna]-V[wiersz][kolumna]))

    if max(testDoZakonczenia) < 10**-4:
        print("Ilosc iteracji: ", i+1)
        print("Mapa potencjalow: ")
        for s in V:print(s)
        print("Polityka ruchu: ")
        for s in politykaRuchu:print(s)
        break
    else:
        testDoZakonczenia.clear()


#print(V)
#print(politykaRuchu)






