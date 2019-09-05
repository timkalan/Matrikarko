import bottle
from model import Matrika, prepoznaj_matriko

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna_stran.tpl")

#OPERACIJE

@bottle.get("/sestevanje")
def sestevanje():
    return bottle.template("operacije.tpl", operacija="/sestej", operator="+")

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
    return bottle.template("operacije.tpl", operacija="/odstej", operator="-")

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
    return bottle.template("operacije.tpl", operacija="/sestej", operator="+")

@bottle.get("/zmnozi")
def zmnozi():
    matrika1_besedilo = bottle.request.query["matrika1"]
    matrika2_besedilo = bottle.request.query["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    zmnozek = matrika1 * matrika2
    return bottle.template("racuni.tpl", rezultat=zmnozek)

#RAČUNANJE Z MATRIKO SAMO

@bottle.get("/sledenje")
def sledenje():
    return bottle.template("matrike.tpl", proces="/sled")

@bottle.get("/sled")
def sled():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    sled = matrika.sled()
    return bottle.template("procesi.tpl", rezultat=sled)

@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template("matrike.tpl", proces="/transponiranka")

@bottle.get("/transponiranka")
def transponiranka():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    transponiranka = matrika.transponiraj()
    return bottle.template("procesi.tpl", rezultat=transponiranka)

@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template("matrike.tpl", proces="/determinanta")

@bottle.get("/determinanta")
def determinanta():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    determinanta = matrika.determinanta()
    return bottle.template("procesi.tpl", rezultat=determinanta)

@bottle.get("/obracanje")
def obracanje():
    return bottle.template("matrike.tpl", proces="/inverz")

@bottle.get("/inverz")
def inverz():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    inverz = matrika.inverz()
    return bottle.template("procesi.tpl", rezultat=inverz)

#LASTNOSTI MATRIK

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("normal.tpl", lastnost="/normalna")

@bottle.get("/normalna")
def normalna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.normalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="normalna")
    
@bottle.get("/simetricnost")
def simetricnost():
    return bottle.template("normal.tpl", lastnost="/simetricna")

@bottle.get("/simetricna")
def simetricna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.simetricna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="simetricna")

@bottle.get("/ortogonalnost")
def ortogonalnost():
    return bottle.template("normal.tpl", lastnost="/ortogonalna")

@bottle.get("/ortogonalna")
def ortogonalna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.ortogonalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="ortogonalna")




bottle.run(reloader=True, debug=True)
 