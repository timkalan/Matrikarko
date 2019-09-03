from model import Matrika

def pozdrav():
    print("""
Ahoj, tu sem, da te rešim dolgočasnih delov linearne algebre!
POZOR! Matrike piši tako, da elemente iste vrstice ločiš s presledkom, vrstice pa z vejicami.
Identiteta recimo izgleda takole: 1 0 0, 0 1 0, 0 0 1 \n""")

def izberi(mozni_odgovori):
    for indeks, odgovor in enumerate(mozni_odgovori):
        print('{}) {}'.format(indeks + 1, odgovor))
    izbira = input('-> ')
    return int(izbira) - 1

def meni():
    print("Kako ti lahko danes pomagam?")
    izbira = izberi([
        "seštej",
        "odštej",
        "pomnoži (s skalarjem ali drugo matriko)",
        "sledi (izračunaj sled)",
        "transponiraj",
        "determiniraj (izračunaj determinanto)",
        "obrni (poišči inverz, če obstaja)",
        "ugotovi določene lastnosti matrik",
        "reši sistem n enačb z n neznankami"
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
    elif izbira == 7:
        meni_lastnosti()
    elif izbira == 8:
        cramer()
    else:
        assert False

def meni_lastnosti():
    print("\nUgotovim lahko naslednje: ")
    izbira = izberi([
        "preveri normalnost", 
        "preveri simetričnost", 
        "preveri ortogonalnost"
    ])

    if izbira == 0:
        normalna()
    elif izbira == 1:
        simetricna()
    elif izbira == 2:
        ortogonalna()
    else:
        assert False

def prepoznaj_matriko(matrika):
    matrika = matrika.split(",")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [int(x) for x in vrstica]
        matrika1.append(vrstica)
    return Matrika(matrika1)

def sestej():
    matrika1 = input("Navedi prvo matriko, ki jo želiš sešteti: ")
    matrika1 = prepoznaj_matriko(matrika1)
    
    matrika2 = input("Navedi drugo matriko, ki jo želiš sešteti: ")
    matrika2 = prepoznaj_matriko(matrika2)
    print(matrika1 + matrika2)
    
def odstej():
    matrika1 = input("Navedi matriko, od katere želiš odštevati: ")
    matrika1 = prepoznaj_matriko(matrika1)

    matrika2 = input("Navedi matriko, ki jo želiš odšteti: ")
    matrika2 = prepoznaj_matriko(matrika2) * -1
    print(matrika1 + matrika2)

def pomnozi():
    matrika1 = input("Navedi prvo matriko, ki jo želiš množiti: ")
    matrika1 = prepoznaj_matriko(matrika1)

    matrika2 = input("Navedi drugo matriko, ki jo želiš množiti: ")
    matrika2 = prepoznaj_matriko(matrika2)
    print(matrika1 + matrika2)

def sled():
    matrika = input("Navedi matriko, katere sled želiš izračunati: ")
    matrika1 = prepoznaj_matriko(matrika)
    print(matrika1.sled())

def transponiraj():
    matrika = input("Navedi matriko, ki jo želiš transponirarti: ")
    matrika1 = prepoznaj_matriko(matrika)
    print(matrika1.transponiraj())

def determinanta():
    matrika = input("Navedi matriko, katere determinanto želiš izračunati: ")
    matrika1 = prepoznaj_matriko(matrika)
    print(matrika1.determinanta())

def inverz():
    matrika = input("Navedi matriko, ki jo želiš obrniti: ")
    matrika1 = prepoznaj_matriko(matrika)
    print(matrika1.inverz())

def normalna():
    matrika = input("Navedi matriko, katere normalnost želiš preveriti: ")
    matrika1 = prepoznaj_matriko(matrika)
    if matrika1.normalna():
        print("Matrika JE normalna!")
    else:
        print("Matrika NI normalna!")

def simetricna():
    matrika = input("Navedi matriko, katere simetričnost želiš preveriti: ")
    matrika1 = prepoznaj_matriko(matrika)
    if matrika1.simetricna():
        print("Matrika JE simetrična!")
    else:
        print("Matrika NI simetrična!")

def ortogonalna():
    matrika = input("Navedi matriko, katere normalnost želiš preveriti: ")
    matrika1 = prepoznaj_matriko(matrika)
    if matrika1.ortogonalna():
        print("Matrika JE ortogonalna!")
    else:
        print("Matrika NI ortogonalna!")

def cramer():
    pass

def main():
    pozdrav()
    while True:
        meni()

main()
