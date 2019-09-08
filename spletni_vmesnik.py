import bottle
from model import Matrika, prepoznaj_matriko, prepoznaj_vektor

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna_stran.tpl")

# OPERACIJE

@bottle.get("/sestevanje")
def sestevanje():
    return bottle.template("operacije.tpl", operacija="/sestej", operator="+", operiraj="SEŠTEJ")

@bottle.get("/sestej")
def sestej():
    matrika1_besedilo = bottle.request.query["matrika1"]
    matrika2_besedilo = bottle.request.query["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 + matrika2
    return bottle.template("racuni.tpl", rezultat=vsota)

@bottle.get("/odstevanje")
def odstevanje():
    return bottle.template("operacije.tpl", operacija="/odstej", operator="-", operiraj="ODŠTEJ")

@bottle.get("/odstej")
def odstej():
    matrika1_besedilo = bottle.request.query["matrika1"]
    matrika2_besedilo = bottle.request.query["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 - matrika2
    return bottle.template("racuni.tpl", rezultat=vsota)

@bottle.get("/mnozenje")
def mnozenje():
    return bottle.template("operacije.tpl", operacija="/sestej", operator="*", operiraj="POMNOŽI")

@bottle.get("/zmnozi")
def zmnozi():
    matrika1_besedilo = bottle.request.query["matrika1"]
    matrika2_besedilo = bottle.request.query["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    zmnozek = matrika1 * matrika2
    return bottle.template("racuni.tpl", rezultat=zmnozek)

# RAČUNANJE Z MATRIKO SAMO

@bottle.get("/sledenje")
def sledenje():
    return bottle.template("matrike.tpl", proces="/sled", racunam="SLED")

@bottle.get("/sled")
def sled():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.sled()
    return bottle.template("procesi.tpl", rezultat=rezultat)

@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template("matrike.tpl", proces="/transponiranka", racunam="TRANSPONIRAJ")

@bottle.get("/transponiranka")
def transponiranka():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.transponiraj()
    return bottle.template("procesi.tpl", rezultat=rezultat)

@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template("matrike.tpl", proces="/determinanta", racunam="DETERMINANTA")

@bottle.get("/determinanta")
def determinanta():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.determinanta()
    return bottle.template("procesi.tpl", rezultat=rezultat)

@bottle.get("/obracanje")
def obracanje():
    return bottle.template("matrike.tpl", proces="/inverz", racunam="INVERZ")

@bottle.get("/inverz")
def inverz():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.inverz()
    return bottle.template("procesi.tpl", rezultat=rezultat)

# FUNKCIJE, KI ZAHTEVANJO VEKTORJE

@bottle.get("/vektorji")
def sistemi():
    return bottle.template("vektorji.tpl", kater="/uporabi", kaj1="Matrika:", kaj2="Vektor:")

@bottle.get("/uporabi")
def cramer():
    matrika_besedilo = bottle.request.query["matrika"]
    vektor_besedilo = bottle.request.query["vektor"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    vektor = prepoznaj_vektor(vektor_besedilo)
    resitev = matrika.uporabi(vektor)
    return bottle.template("racuni.tpl", rezultat=resitev)

@bottle.get("/sistemi")
def sistemi():
    return bottle.template("vektorji.tpl", kater="/cramer", kaj1="Matrika sistema (kvadratna!!):", kaj2="Vektor (desna stran sistema):")

@bottle.get("/cramer")
def cramer():
    matrika_besedilo = bottle.request.query["matrika"]
    vektor_besedilo = bottle.request.query["vektor"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    vektor = prepoznaj_vektor(vektor_besedilo)
    resitev = matrika.cramer(vektor)
    return bottle.template("racuni.tpl", rezultat=resitev)

# LASTNOSTI MATRIK

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("normal.tpl", lastnost="/normalna", poglej="NORMALNOST")

@bottle.get("/normalna")
def normalna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.normalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="normalna")
    
@bottle.get("/simetricnost")
def simetricnost():
    return bottle.template("normal.tpl", lastnost="/simetricna", poglej="SIMETRIČNOST")

@bottle.get("/simetricna")
def simetricna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.simetricna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="simetrična")

@bottle.get("/ortogonalnost")
def ortogonalnost():
    return bottle.template("normal.tpl", lastnost="/ortogonalna", poglej="ORTOGONALNOST")

@bottle.get("/ortogonalna")
def ortogonalna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.ortogonalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="ortogonalna")

# ZA SLIKE

@bottle.get('/img/<ime>')
def slike(ime):
   return bottle.static_file(ime, root = 'img')


bottle.run(reloader=True, debug=True)
