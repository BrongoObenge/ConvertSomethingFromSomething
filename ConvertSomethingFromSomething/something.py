__author__ = 'j'
import csv
from Domain import Persoon
from Convert import ConvertSomeWord as C, Filter
from Manager import DBMan

csvfile1 = "/home/j//Desktop/OFD/1.csv"
csvfile2 = "/home/j//Desktop/OFD/2.csv"
csvfile3 = "/home/j//Desktop/OFD/3.csv"

persoonLijst = []
db_man = DBMan.DBStuff()
db = db_man.openDB()
def importVkg(location):
    with open(location, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            naam = C.convertRelatie(row.get("Relatie"))
            postcode = C.convertPostcode(row.get("Postcode"))
            address = C.convertAdres(row.get("Adres"))
            persoonLijst.append(Persoon.Persoon(
                            voornaam = naam["voornaam"],
                            achternaam = naam["achternaam"],
                            geslacht = row.get("Geslacht"),
                            email = row.get("Email"),
                            woonplaats = row.get("Plaats").replace("'", ""),
                            maatschappij = row.get("Maatschappij"),
                            klantnummer = row.get("Relatienummer"),
                            postcode = postcode["postcode"],
                            straat = address["adres"],
                            huisnummer = address["huisnummer"],
                            toevoeging = address["toevoegsel"],
                            telefoonnummer = row.get("Telefoon")))

    Filter.filterListOnUnique(persoonLijst)
    for persoon in persoonLijst:
        db_man.addPersoonToDb(db, persoon)
def importVoogd(location):
    with open(location, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:

            geslacht = row.get("Geslacht")
            if geslacht not in ["M", "V"]:
                geslacht = "NULL"
            persoonLijst.append(Persoon.Persoon(
                            voornaam=row.get("Voorletters"),
                            achternaam=row.get("Achternaam"),
                            geslacht=geslacht,
                            email=row.get("Email"),
                            woonplaats=row.get("Woonplaats").replace("'", ""),
                            maatschappij=row.get("Maatschappij Naam"),
                            klantnummer=row.get("Klant Nr "),
                            postcode=row.get("Postcode")[0],
                            straat=row.get("Straat"),
                            huisnummer=row.get("Huis Nr"),
                            toevoeging=row.get("Huis Nr Toevoegsel"),
                            telefoonnummer=row.get("Telefoon Nr")))

    Filter.filterListOnUnique(persoonLijst)

    for persoon in persoonLijst:
        db_man.addPersoonToDb(db, persoon)

if __name__ == "__main__":
    importVkg(csvfile1)
    importVoogd(csvfile2)
    importVoogd(csvfile3)
