from copy import deepcopy
def wybierzNajlepszaAkcje(rozmiar, mapa, V, R, y):
    vs = deepcopy(R)
    mapaRuchu = []
    for wiersz in range(rozmiar[1]):
        mapaRuchu.append([0]*rozmiar[0])

    #print(mapaRuchu)
    #mapaRuchu = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    #print(mapaRuchu)
    lewo = 0
    prawo = 0
    gora = 0
    for wiersz in range(rozmiar[1]):
        for kolumna in range(rozmiar[0]):
            if mapa[wiersz][kolumna] == 1:
                #print("Znalazlem {} {}".format(wiersz, kolumna))

                # obliczamy gore

                if kolumna == 0 or mapa[wiersz][kolumna-1] == 0:
                    lewo = V[wiersz][kolumna] * 0.1
                else:
                    lewo = V[wiersz][kolumna - 1] * 0.1
                if wiersz == 0 or mapa[wiersz-1][kolumna] == 0:
                    gora = V[wiersz][kolumna] * 0.8
                else:
                    gora = V[wiersz - 1][kolumna] * 0.8
                if kolumna == rozmiar[0]-1 or mapa[wiersz][kolumna+1] == 0:
                    prawo = V[wiersz][kolumna] * 0.1
                else:
                    prawo = V[wiersz][kolumna + 1] * 0.1

                ruchGora = lewo + gora + prawo
                #print("ruch w gore ", ruchGora)

                #obliczamy prawo

                if wiersz == 0 or mapa[wiersz-1][kolumna] == 0:
                    lewo = V[wiersz][kolumna] * 0.1
                else:
                    lewo = V[wiersz - 1][kolumna] * 0.1
                if kolumna == rozmiar[0]-1 or mapa[wiersz][kolumna+1] == 0:
                    gora = V[wiersz][kolumna] * 0.8
                else:
                    gora = V[wiersz][kolumna + 1] * 0.8
                if wiersz == rozmiar[1]-1 or mapa[wiersz+1][kolumna] == 0:
                    prawo = V[wiersz][kolumna] * 0.1
                else:
                    prawo = V[wiersz + 1][kolumna] * 0.1

                ruchPrawo = lewo + gora + prawo
                #print("ruch w prawo ", ruchPrawo)

                # obliczamy dol

                if kolumna == rozmiar[0]-1 or mapa[wiersz][kolumna+1] == 0:
                    lewo = V[wiersz][kolumna] * 0.1
                else:
                    lewo = V[wiersz][kolumna + 1] * 0.1
                if wiersz == rozmiar[1]-1 or mapa[wiersz+1][kolumna] == 0:
                    gora = V[wiersz][kolumna] * 0.8
                else:
                    gora = V[wiersz + 1][kolumna] * 0.8
                if kolumna == 0 or mapa[wiersz][kolumna-1] == 0:
                    prawo = V[wiersz][kolumna] * 0.1
                else:
                    prawo = V[wiersz][kolumna - 1] * 0.1

                ruchDol = lewo + gora + prawo
                #print("ruch w dol ", ruchDol)

                # obliczamy lewo

                if wiersz == rozmiar[1]-1 or mapa[wiersz+1][kolumna] == 0:
                    lewo = V[wiersz][kolumna] * 0.1
                else:
                    lewo = V[wiersz + 1][kolumna] * 0.1
                if kolumna == 0 or mapa[wiersz][kolumna-1] == 0:
                    gora = V[wiersz][kolumna] * 0.8
                else:
                    gora = V[wiersz][kolumna - 1] * 0.8
                if wiersz == 0 or mapa[wiersz-1][kolumna] == 0:
                    prawo = V[wiersz][kolumna] * 0.1
                else:
                    prawo = V[wiersz - 1][kolumna] * 0.1

                ruchLewo = lewo + gora + prawo

                #print("ruch w lewo ", ruchLewo)
                listaRuchow = [ruchGora, ruchPrawo, ruchDol, ruchLewo]
                #print(listaRuchow)
                najlepszaAkcja = listaRuchow.index(max(listaRuchow))+1
                #print(listaRuchow,najlepszaAkcja)
                mapaRuchu[wiersz][kolumna] = deepcopy(najlepszaAkcja)
                #print(najlepszaAkcja)
                Rdoprzekazania = R[wiersz][kolumna]
                potencjal = Rdoprzekazania + y * max(listaRuchow)
                #print(potencjal)
                vs[wiersz][kolumna] = potencjal

    zwrot = [mapaRuchu, vs]

    return zwrot


#rozmiar1 = [4, 3]
#mapa1 = [[1, 1, 1, 2], [1, 0, 1, 2], [1, 1, 1, 1]]
#V1 = [[-1, -1, -1, 100], [-1, 0, -1, -80], [-1, -1, -1, -1]]
#R1 = [[-1, -1, -1, 100], [-1, 0, -1, -80], [-1, -1, -1, -1]]
#vs = [[-1, -1, -1, 100], [-1, 0, -1, -80], [-1, -1, -1, -1]]
#mapaRuchu = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#y1 = 0.5
#test = wybierzNajlepszaAkcje(rozmiar1, mapa1, V1, R1, y1)
#V1 = test[1]
#for i in range(5):
#    test = wybierzNajlepszaAkcje(rozmiar1, mapa1, V1, R1, y1)
#    V1 = test[1]
#    print(test)
