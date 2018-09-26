#---------------- Import ----------------
from datetime import datetime
import calendar

#---------------- Fonction Vérification -------------
def verificationFormat():
    # -- On demande une date à un certain format
    dateVerif = input("Entrez la date voulu (jj/mm/aaaa) à partir du 1er novembre 1582 :\n")

    # -- On regarde si le format est respecter
    try :
        datetime.strptime(dateVerif, '%d/%m/%Y')
        dateVerif = dateVerif.replace('/', '')
    # -- On regarde si la date nest supérieur à 1582
        if int(dateVerif[4:])>1582:
            calculJour(dateVerif)
        # -- On regarde si la date n'est pas inférieur à 11/1582
        elif int(dateVerif[4:])==1582:
            if int(dateVerif[2:4]) > 10:
                calculJour(dateVerif)
            else:
                raise ValueError
        else:
            raise ValueError
    # -- Si il y a une erreur, on affiche un message
    except ValueError:
        print("Date Invalide, veuillez retenter ! \n")

#---------------- Fonction Calcul -------------
def calculJour(date):
    #Variables qui seront utiliser pour les calculs
    siecleBis=15
    resBis=0
    valeurMois=[0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5] #Allant de Janvier à Décembre

    # Variables qui seront utiliser pour l'affichage
    affJour = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
    affMois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

    #On divise toutes les parties nécessaires aux calculs
    jour=int(date[:2])
    mois=int(date[2:4])
    siecle=int(date[4:6])
    annee=int(date[6:])

    print("\n")
    resultat=annee
    print("Étape 1 : ", resultat)

    resultat+=int(annee/4)
    print("Étape 2 : ", resultat)

    resultat+=jour
    print("Étape 3 : ", resultat)

    resultat+=valeurMois[mois - 1]
    print("Étape 4 : ", resultat)

    #On regarde si l'année est bissextile
    if calendar.isleap(int(date[4:]))and(mois == 1 or mois == 2):
        resultat+= -1
    print("Étape 5 : ", resultat)

    #On crée une suite logique selon le siècle (0, 6, 4, 2)
    while siecleBis != siecle :
        if resBis<=0:
            resBis=8
        resBis+=-2
        siecleBis += 1

    resultat+=resBis
    print("Étape 6 : ", resultat)

    resultat=resultat%7
    print("Étape Final : ", resultat, "\n")
    print("Le ",date[:2]," ",affMois[mois-1]," ",date[4:]," est un ",affJour[resultat],"\n")


while 1:
    dateVerifier=verificationFormat()

