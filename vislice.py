import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'U:\\Niki (UVP)\\Repozitorij\\Vislice\\views')

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    return bottle.template('igra.tpl',
    igra = vislice.igre[id_igre][0],
    id_igre = id_igre,
    poskus = vislice.igre[id_igre][1])

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka_za_ugib = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka_za_ugib)
    bottle.redirect('/igra/{0}/'.format(id_igre))

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root = 'img')


bottle.run(reloader=True, debug=True)