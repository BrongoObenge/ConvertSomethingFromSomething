__author__ = 'j'
def mergeArrays(mergeTo, a2):
    for x in a2:
        mergeTo.append(x)
    return mergeTo
def filterListOnUnique(persoonLijst):
    for p1 in persoonLijst:
        for p2 in persoonLijst:
            if compare(p1, p2):
                persoonLijst.remove(p2)
    return persoonLijst

def compare(p1, p2):
    if p1.klantnummer == p2.klantnummer:
        return True
    return False