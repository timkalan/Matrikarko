# import bottle
import model

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

# zdej morš še definirat vse te funkcije

def sestej():
    pass

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


def pozeni_vmesnik():
    # to je glavni program, heh
    pass
