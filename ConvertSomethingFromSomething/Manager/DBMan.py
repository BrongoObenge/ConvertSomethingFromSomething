__author__ = 'j'
from Config import Config as c
import MySQLdb
from time import strftime

class DBStuff:
    def __init__(self):
        pass
    def openDB(self):
        db = MySQLdb.connect(host= c.CONNECTION_URL,
                      user= c.CONNECTION_USERNAME,  # your username
                      passwd= c.CONNECTION_PASSWORD,  # your password
                      db= c.DATABASE_NAME)  # name of the data base
        db.autocommit(True)
        return db

    def closeDB(self, db):
        db.close()

    def executeQuery(self, db, query):
        cur = db.cursor()
        cur.execute(query)
        return cur

    def getTimestamp(self):
        return strftime("%Y-%m-%d %H:%M:%S")

    def addPersoonToDb(self, db, persoon):
        #TODO use ORM
        temp_select_persoon = "SELECT "+c.PERSOON_ID +" FROM `"+c.DATABASE_NAME+"`.`"+c.PERSOON_TABLE+"` " \
             "WHERE "+c.PERSOON_POSTCODE+" = '{a}' AND " \
             +c.PERSOON_VOORLETTERS+" = '{b}' AND "+c.PERSOON_ACHTERNAAM+" = '{c}';"

        select_persoon = temp_select_persoon.format(a=persoon.postcode, b=persoon.voornaam, c=persoon.achternaam)

        select_maatschappij = "SELECT "+c.MAATSCHAPPIJ_ID+" FROM `"+c.MAATSCHAPPIJ_TABLE+"` " \
             "WHERE `"+c.MAATSCHAPPIJ_NAAM+"` = '{0}';".format(persoon.maatschappij)

        select_klant = "SELECT "+c.KLANT_ID+" FROM `"+c.KLANT_TABLE+"` " \
             "WHERE `"+c.KLANT_MAATSCHAPPIJID+"` = '{0}' AND " \
             "`"+c.KLANT_PERSOONID+"` = '{1}';"

        insert_persoon = "INSERT INTO `"+c.DATABASE_NAME+"`.`"+c.PERSOON_TABLE+"` (`"+c.PERSOON_VOORLETTERS+"`," \
             " `"+c.PERSOON_ACHTERNAAM+"`, `"+c.PERSOON_STRAAT+"`, `"+c.PERSOON_HUISNUMMER+"`, `"+c.PERSOON_TOEVOEGSEL+"`, " \
             "`"+c.PERSOON_POSTCODE+"`, `"+c.PERSOON_WOONPLAATS+"`, `"+c.PERSOON_EMAIL+"`, `"+c.PERSOON_TELEFOONNUMMER+"`, " \
             " `"+c.PERSOON_GESLACHT+"`) " \
             "VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}');".format(persoon.voornaam,
             persoon.achternaam, persoon.straat, persoon.huisnummer, persoon.toevoeging, persoon.postcode, persoon.woonplaats,
             persoon.email, persoon.telefoonnummer, persoon.geslacht)

        insert_maatschappij = "INSERT INTO `"+c.DATABASE_NAME+"`.`"+c.MAATSCHAPPIJ_TABLE+"` (`"+c.MAATSCHAPPIJ_NAAM+"`)" \
             " VALUES ('{0}');".format(persoon.maatschappij)

        insert_klant = "INSERT INTO `"+c.DATABASE_NAME+"`.`"+c.KLANT_TABLE+"` (`"+c.KLANT_KLANTNUMMER+"`, " \
             "`"+c.KLANT_MAATSCHAPPIJID+"`, `"+c.KLANT_PERSOONID+"`) " \
             "VALUES ('"+persoon.klantnummer+"', '{0}', {1});"




        persoon_id = self.getId(db, select_persoon)
        maatschappij_id = self.getId(db, select_maatschappij)

        if persoon_id is None:
            print insert_persoon
            self.executeQuery(db, insert_persoon)
        if maatschappij_id is None:
            self.executeQuery(db, insert_maatschappij)

        if persoon_id is None:
            persoon_id = self.getId(db, select_persoon)
        if maatschappij_id is None:
            maatschappij_id = self.getId(db, select_maatschappij)

        if self.getId(db, select_klant.format(maatschappij_id, persoon_id)) is None:
            self.executeQuery(db, insert_klant.format(maatschappij_id, persoon_id))

    def getId(self, db, q):
        cur = self.executeQuery(db, q)
        if cur.rowcount > 0:
            row = cur.fetchone()
            return row[0]
        return None