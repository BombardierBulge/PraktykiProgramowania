import string

def add(abc):
    if abc == "":
        return 0
    liczby = abc.split(',')
    wynik = 0
    for x in liczby:
        x= x.split('\n')
        for y in x:
            wynik += int(y)
    return(wynik)
