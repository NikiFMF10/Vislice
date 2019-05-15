STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'O' 
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:

    def __init__(self, geslo, crke = None ):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
            else:
                pass
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        delni = ""
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni


testno_geslo = "požrtvovalnost"
testne_crke = ["a", "e", "o", "p"]
zmagovalne_crke = [x for x in testno_geslo]
igra = Igra(testno_geslo, testne_crke)
print(igra.napacne_crke())
print(igra.pravilne_crke())
print(igra.stevilo_napak())
print(igra.zmaga())
zmagana_igra = Igra(testno_geslo, zmagovalne_crke)
print(zmagana_igra.zmaga())
print(igra.poraz())
print(igra.pravilni_del_gesla())        