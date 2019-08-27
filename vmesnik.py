# import bottle
#import model
from model import Matrika

""" hahahahaha kaj sploh hahahahahah """

def pozdrav():
    print("Ahoj, tu sem, da te rešim dolgočasnih delov linearne algebre!")

def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('-> ')
    return int(izbira) - 1

def meni():
    print("Pomagam ti lahko z:")
    izbira = izberi([
        "seštej",
        "odštej",
        "pomnoži (s skalarjem ali drugo matriko)",
        "sledi (izračunaj sled)",
        "transponiraj",
        "determiniraj (izračunaj determinanto)",
        "obrni (poišči inverz, če obstaja)",
    ])

    if izbira == 0:
        sestej()
    elif izbira == 1:
        odstej()
    elif izbira == 2:
        pomnozi()
    elif izbira == 3:
        sled()
    elif izbira == 4:
        transponiraj()
    elif izbira == 5:
        determinanta()
    elif izbira == 6:
        inverz()
    else:
        assert False

def sestej():
    # mogoče je še mal tko eh
    matrika1 = input("Navedi prvo matriko, ki jo želiš sešteti:")
    matrika1 = matrika1.split(",")
    prva_matrika = []
    for vrstica in matrika1:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        prva_matrika.append(vrstica)
    prva_matrika = Matrika(prva_matrika)

    matrika2 = input("Navedi drugo matriko, ki jo želiš sešteti:")
    matrika2 = matrika2.split(",")
    druga_matrika = []
    for vrstica in matrika2:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        druga_matrika.append(vrstica)
    druga_matrika = Matrika(druga_matrika)
    print(prva_matrika + druga_matrika)
    

def odstej():
    pass

def pomnozi():
    pass

def sled():
    pass

def transponiraj():
    pass

def determinanta():
    pass

def inverz():
    pass

def zahtevaj_vnos():
    return input("Vpišite matriko: ")

def izpis_rezultata(matrika):
    izpis = "{0}\n".format(matrika)
    return izpis


def main():
    # to je glavni program, heh
    pozdrav()
    while True:
        meni()

main()
