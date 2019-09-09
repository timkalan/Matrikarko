import bottle
from model import Matrika

# SPORAZUMEVANJE Z MODELOM

def prepoznaj_matriko(matrika):
    """ V spletnem vmesniku pretvori uporabnikov vnos v 
        modelu razumljivo matriko. """

    matrika = matrika.split("\n")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [float(x) for x in vrstica]
        matrika1.append(vrstica)
    return Matrika(matrika1)

def prepoznaj_vektor(vektor):
    """ Malce preprostejša verzija zgornje funkcije, vnos spremeni
        v vektor (seznam). """

    vektor = vektor.split(" ")
    vektor = [float(i) for i in vektor]
    return vektor

# OSNOVA

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna_stran.tpl")

# OPERACIJE

@bottle.get("/sestevanje")
def sestevanje():
    return bottle.template("operacije.tpl", operacija="/sestej", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestej")
def sestej():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 + matrika2
    return bottle.template("racuni.tpl", rezultat=vsota)

@bottle.get("/odstevanje")
def odstevanje():
    return bottle.template("operacije.tpl", operacija="/odstej", operator="-", operiraj="ODŠTEJ")

@bottle.post("/odstej")
def odstej():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 - matrika2
    return bottle.template("racuni.tpl", rezultat=vsota)

@bottle.get("/mnozenje")
def mnozenje():
    return bottle.template("operacije.tpl", operacija="/zmnozi", operator="*", operiraj="POMNOŽI")

@bottle.post("/zmnozi")
def zmnozi():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    zmnozek = matrika1 * matrika2
    return bottle.template("racuni.tpl", rezultat=zmnozek)

# RAČUNANJE Z MATRIKO SAMO

@bottle.get("/sledenje")
def sledenje():
    return bottle.template("matrike.tpl", proces="/sled", racunam="SLED")

@bottle.post("/sled")
def sled():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.sled()
    return bottle.template("procesi.tpl", rezultat=rezultat)

@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template("matrike.tpl", proces="/transponiranka", racunam="TRANSPONIRAJ")

@bottle.post("/transponiranka")
def transponiranka():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.transponiraj()
    return bottle.template("procesi.tpl", rezultat=rezultat)

@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template("matrike.tpl", proces="/determinanta", racunam="DETERMINANTA")

@bottle.post("/determinanta")
def determinanta():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.determinanta()
    return bottle.template("procesi.tpl", rezultat=rezultat)

@bottle.get("/obracanje")
def obracanje():
    return bottle.template("matrike.tpl", proces="/inverz", racunam="INVERZ")

@bottle.post("/inverz")
def inverz():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.inverz()
    return bottle.template("procesi.tpl", rezultat=rezultat)

# FUNKCIJE, KI ZAHTEVAJO VEKTORJE

@bottle.get("/vektorji")
def vektorji():
    return bottle.template("vektorji.tpl", 
                            kater="/uporabi", 
                            kaj1="Matrika:", 
                            kaj2="Vektor:", 
                            delaj="UPORABI", 
                            opis="Preslikaj vektor z linearno preslikavo, ki jo predstavlja matrika.")

@bottle.post("/uporabi")
def uporabi():
    matrika_besedilo = bottle.request.forms["matrika"]
    vektor_besedilo = bottle.request.forms["vektor"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    vektor = prepoznaj_vektor(vektor_besedilo)
    resitev = matrika.uporabi(vektor)
    return bottle.template("vektor_rezultati.tpl", rezultat=resitev)

@bottle.get("/sistemi")
def sistemi():
    return bottle.template("vektorji.tpl", 
                            kater="/cramer", 
                            kaj1="Matrika sistema (kvadratna!):",
                            kaj2="Vektor (b1, b2, b3, ...):", 
                            delaj="REŠI",
                            opis="S Cramerjevim pravilom reši sistem Ax = b, kjer je A matrika in b vektor, ki ga vpisuješ. Rezultat je podan kot vektor neznank; x = [x1, x2, x3, ...].")

@bottle.post("/cramer")
def cramer():
    matrika_besedilo = bottle.request.forms["matrika"]
    vektor_besedilo = bottle.request.forms["vektor"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    vektor = prepoznaj_vektor(vektor_besedilo)
    resitev = matrika.cramer(vektor)
    return bottle.template("vektor_rezultati.tpl", rezultat=resitev)

# LASTNOSTI MATRIK

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("normal.tpl", lastnost="/normalna", poglej="NORMALNOST")

@bottle.post("/normalna")
def normalna():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.normalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="normalna")
    
@bottle.get("/simetricnost")
def simetricnost():
    return bottle.template("normal.tpl", lastnost="/simetricna", poglej="SIMETRIČNOST")

@bottle.post("/simetricna")
def simetricna():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.simetricna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="simetrična")

@bottle.get("/ortogonalnost")
def ortogonalnost():
    return bottle.template("normal.tpl", lastnost="/ortogonalna", poglej="ORTOGONALNOST")

@bottle.post("/ortogonalna")
def ortogonalna():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.ortogonalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="ortogonalna")

# ZA SLIKE

@bottle.get('/img/<ime>')
def slike(ime):
   return bottle.static_file(ime, root = 'img')


bottle.run(reloader=True, debug=True)
