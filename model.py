STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'o' 
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

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
             


testno_geslo = "požrtvovalnost".upper()
testne_crke = ["A", "E", "O", "P"]
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
print(igra.nepravilni_ugibi())
poskus = igra.ugibaj("r")
print(poskus)
print(igra.pravilni_del_gesla())
poskus = igra.ugibaj("e")
print(poskus)
print(igra.pravilni_del_gesla())
poskus = igra.ugibaj("x")
print(poskus)
print(igra.napacne_crke())            