import bottle
from model import Matrika, prepoznaj_matriko

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna_stran.tpl")

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("normal.tpl")

@bottle.get("/normalnost_post")
def normalna():
    matrika_besedilo = bottle.request.query["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    preveri = matrika.normalna()
    return bottle.template("lastnosti.tpl", preveri=preveri, lastnost="normalnost")
    









@bottle.get("/simetricnost")
def simetricnost():
    return "ja pač tukej bo zdej neki neki"

@bottle.get("/ortogonalnost")
def ortogonalnost():
    return "ja pač tukej bo zdej neki neki"





bottle.run(debug=True, reloader=True)
 