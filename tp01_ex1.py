"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.

1J  =  0.738 ft-lb  =  0.239 cal  =  6.24*10^18 eV

Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variable

joule: int = 1
ftlb: float = 0.738
cal : float = 0.239
eV : float = 6.24 * (10**18)
qte=None
### Séquence d'opération

nb_ent : float = float(input("Quantité d'énergie a convertir"))
qte : str=input("Unité (j ft-lb cal eV)")

if qte == "J" or qte == "j":
    print("\nValeur en entrée :",str(nb_ent),"J")
    print("------------conversion------------")
    print("en ft-lb : " ,nb_ent * ftlb," ft-lb")
    print("en calories : " ,nb_ent * cal," cal")
    print("en eV : " ,nb_ent * eV," eV")


elif qte == "eV" :
    print("en ft-lb" ,nb_ent / eV * ftlb )
    print("en cal" ,nb_ent / eV * cal)
    print("en j" ,nb_ent / eV)
else:
    print ("end")