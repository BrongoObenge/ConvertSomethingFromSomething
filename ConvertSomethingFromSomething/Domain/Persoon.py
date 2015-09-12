__author__ = 'j'
class Persoon:
    voornaam = None
    achternaam = None
    geslacht = None
    email = None
    woonplaats = None
    maatschappij = None
    klantnummer = None
    postcode = None
    straat = None
    huisnummer = None
    toevoeging = None
    telefoonnummer = None


    def __init__(self, voornaam, achternaam, geslacht, email, woonplaats, maatschappij, klantnummer, postcode, straat,
                 huisnummer, toevoeging, telefoonnummer):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.geslacht = geslacht
        self.email = email
        self.woonplaats = woonplaats
        self.maatschappij = maatschappij
        self.klantnummer = klantnummer
        self.postcode = postcode
        self.straat = straat
        self.huisnummer = huisnummer
        self.toevoeging = toevoeging
        self.telefoonnummer = telefoonnummer

    def printPersoon(self):
        print "voornaam: ", self.voornaam
        print "achternaam: ", self.achternaam
        print "geslacht: ", self.geslacht
        print "email: ", self.email
        print "woonplaats: ", self.woonplaats
        print "maatschappij: ", self.maatschappij
        print "klantnummer: ", self.klantnummer
        print "postcode: ", self.postcode
        print "straat: ", self.straat
        print "huisnummer: ", self.huisnummer
        print "toevoeging: ", self.toevoeging
        print "telefoonnummer: ", self.telefoonnummer
