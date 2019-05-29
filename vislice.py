import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'U:\\Niki (UVP)\\Repozitorij\\Vislice\\views')

SKRIVNOST = 'pssst_moja_skrivnost'
DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'
vislice = model.Vislice(DATOTEKA_S_STANJEM, DATOTEKA_Z_BESEDAMI)

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, secret = SKRIVNOST, path = '/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    return bottle.template('igra.tpl',
    igra = vislice.igre[id_igre][0],
    id_igre = id_igre,
    poskus = vislice.igre[id_igre][1])

@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    crka_za_ugib = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka_za_ugib)
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root = 'img')


bottle.run(reloader=True, debug=True)