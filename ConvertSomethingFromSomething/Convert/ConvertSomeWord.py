__author__ = 'j'
import re

def convertRelatie(str):
    r1 = r"(.+)(,.+)(\w+)\.?" #splits Relatie into Achternaam and Voorletter
    result = {}
    m = re.search(r1, str)
    if m:
        result["achternaam"] = m.group(1)
        result["voornaam"] = m.group(3)
    else:
        result["achternaam"] = str
        result["voornaam"] = None

    return result

def convertAdres(string):
    result = {} #adres huisnummer toevoegsel
    r2 = r"(.+\W)(\d+)(.+)?(\w)?"
    r3 = r"^\d"
    r4 = r"(\d+\w\W.+)(\W\d)(.+)?"

    m = re.search(r2, string)
    m2 = re.search(r3, string)

    result["adres"] = None      #Set None before adding value
    result["huisnummer"] = None
    result["toevoegsel"] = None

    if m2:
        m3 = re.search(r4, string)
        result["adres"] = m3.group(1)
        result["huisnummer"] = m3.group(2)
        result["toevoegsel"] = m3.group(3)
    else:
        if m:
            result["adres"] = m.group(1)
            result["huisnummer"] = m.group(2)
            result["toevoegsel"] = str(m.group(3)).replace(" ", "").replace("-", "")

    return result

def convertPostcode(string):
    result = {}
    r5 = r"(\d{4}).(\w{2})"
    m4 = re.search(r5, string)
    if m4:
        result["postcode"] = m4.group(1)+m4.group(2)
    return result

