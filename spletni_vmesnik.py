import bottle
from model import Matrika

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnova.tpl")

bottle.run(debug=True, reloader=True)
 