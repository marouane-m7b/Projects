def paire(nbr:int)->bool:
    if isinstance(nbr,int):
        return nbr % 2 == 0
    else:
        raise ValueError("le parametre doit etre un entier")

try:
    print(paire('4.5'))
except ValueError as e:
    print(e)