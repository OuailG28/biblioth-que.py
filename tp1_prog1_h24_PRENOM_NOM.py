#Nom : GACEM Ouail 

#EXERCICE 1
def Quadrant_Cartesien():
    for x in range(10):  # Parcourt les valeurs de x de 0 à 9
        for y in range(10):  # Parcourt les valeurs de y de 0 à 9
            print(f'({x}, {y})')

# Appel de la fonction
Quadrant_Cartesien()

#EXERCICE 2
def chaine_avancee():
    print("Choisissez une opération :")
    print("1 - Comparaison Alphabétique")
    print("2 - Remplacement de Caractères")
    
    choix = input("Entrez le numéro de l'opération : ")
    
    if choix == "1":
        ch1 = input("Entrez la première chaîne : ")
        ch2 = input("Entrez la deuxième chaîne : ")
        resultat = min(ch1, ch2)
        print(f"La chaîne qui vient en premier est : {resultat}")
    
    elif choix == "2":
        ch = input("Entrez une chaîne de caractères : ")
        char_a_remplacer = input("Entrez le caractère à remplacer : ")
        char_de_remplacement = input("Entrez le caractère de remplacement : ")
        
        if len(char_a_remplacer) != 1 or len(char_de_remplacement) != 1:
            print("Erreur : Veuillez entrer un seul caractère pour le remplacement.")
            return
        
        nouvelle_chaine = ch.replace(char_a_remplacer, char_de_remplacement)
        print(f"La nouvelle chaîne est : {nouvelle_chaine}")
    
    else:
        print("Erreur : Option invalide.")

# Exécution de la fonction
chaine_avancee()

#EXERCICE 3
def calculateur_taux_interet_compose():
    print("Bienvenue dans le calculateur de taux d'intérêt composé!")
    
    # Saisie utilisateur
    a = float(input("Entrez le capital initial (P) : "))
    b = float(input("Entrez le taux d'intérêt annuel en pourcentage (r) : "))
    n = int(input("Entrez le nombre de périodes de composition par an (n) : "))
    t = float(input("Entrez la durée de l'investissement en années (t) : "))
    
    # Conversion du taux d'intérêt en décimal
    b = b / 100
    
    # Calcul de la valeur future
    FV = a * (1 + b / n) ** (n * t)
    
    # Calcul du gain total
    gain_total = FV - a
    
    # Affichage des résultats
    print(f"\nRésultats :")
    print(f"Valeur future de l'investissement : {FV:.2f}")
    print(f"Gain total sur l'investissement : {gain_total:.2f}")
    
# Exécution du programme
calculateur_taux_interet_compose()