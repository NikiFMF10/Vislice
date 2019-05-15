import model

lojtrice = "###########################################################\n"

def izpis_zmage(igra):
    tekst = lojtrice + "Uganili ste geslo {0}.\n".format(igra.geslo)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + "Obešeni ste! Pravilno geslo je bilo {0}.\n".format(igra.geslo)
    return tekst

def izpis_igre(igra):
    tekst = (lojtrice +
            igra.pravilni_del_gesla() + "\n" +
            ("Preostalo število poizkusov: {0}\nNapačni ugibi: {1}\n"
            ).format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
            igra.nepravilni_ugibi()) + lojtrice)
    return tekst

def zahtevaj_vnos():
    return input("Ugibaj črko: ")

def pozeni_vmesnik():

    igra = model.nova_igra()

    while True:
        # Izpisemo stanje igre
        print(izpis_igre(igra))
        # Zahtevaj vnos uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        # Preveri, ali smo končali
        if igra.poraz():
            print(izpis_poraza(igra))
            break
        elif igra.zmaga():
            print(izpis_zmage(igra))
            break
        else:
            pass
    return None


igra = model.nova_igra()
print(izpis_zmage(igra))
print(izpis_poraza(igra))
print(izpis_igre(igra))