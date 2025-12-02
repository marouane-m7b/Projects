pSeuil = 2.3
vSeuil = 7.41

pression = float(input("Entrer Pression : \n"))
volume = float(input("Entrer Volume : \n"))

if pression > pSeuil and volume > vSeuil :
    print("Arret immediat")
elif pression > pSeuil:
    print("Augementer le volume de l'enceinte")
elif volume > vSeuil :
    print("Diminuer le volume de l'enceinte")
else :
    print("Tout va bien")
