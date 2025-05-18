import json
import os
dossier = "bib.json"

def charge():
    if os.path.exists(dossier):
        with open(dossier, "r") as f:
            return json.load(f)
    return []


def display(bibliotéque):
    if not bibliotéque:
        print("Aucun livre.")
    for livre in bibliotéque:
        lu = "Lu" if livre["Lu"] else "Non lu"
        print(f"[{livre['ID']}] {livre['Titre']} - {livre['Auteur']} ({livre['Année']}) - {lu}")

def add(bibliotéque):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = int(input("Année : "))
    new_id = max((l["ID"] for l in bibliotéque), default=0) + 1
    livre = {"ID": new_id, "Titre": titre, "Auteur": auteur, "Année": annee, "Lu": False}
    bibliotéque.append(livre)
    print("📘 Livre ajouté avec succès.")

    #  Création du dossier "livres" si nécessaire
    dossier_livres = "livres"
    if not os.path.exists(dossier_livres):
        os.makedirs(dossier_livres)

    # Enregistrement du livre dans un fichier JSON individuel
    nom_fichier = f"{dossier_livres}/livre_{new_id}.json"
    with open(nom_fichier, "w") as f:
        json.dump(livre, f, indent=2)
    print(f" Fichier '{nom_fichier}' créé.")


def delete(bibliotéque):
    id_ = int(input("ID du livre à delete : "))
    for livre in bibliotéque:
        if livre["ID"] == id_:
            bibliotéque.remove(livre)
            print("Livre supprimé.")
            return
    print("Livre non trouvé.")

def lu(bibliotéque):
    id_ = int(input("ID du livre à marquer comme lu : "))
    for livre in bibliotéque:
        if livre["ID"] == id_:
            livre["Lu"] = True
            print("Livre lu.")
            return
    print("Livre non trouvé .")
def save(bibliotéque):
    with open(dossier, "w") as f:
        json.dump(bibliotéque, f, indent=2)

def search(bibliotéque):
    mot = input("clé (titre ou auteur) : ").lower()
    resultats = [l for l in bibliotéque if mot in l["Titre"].lower() or mot in l["Auteur"].lower()]
    display(resultats)

def affichage():
    bibliotéque = charge()
    while True:
       print("\n" + "="*50)
       print("📚  Bienvenue dans votre Bibliothèque  📚".center(50))
       print("="*50)
       print("👤 Créé par : Ouail Gacem")
       print("\nQue souhaitez-vous faire ?\n")
       print("1️⃣  Afficher les livres")
       print("2️⃣  Ajouter un livre")
       print("3️⃣  Supprimer un livre")
       print("4️⃣  Marquer un livre comme lu")
       print("5️⃣  Rechercher un livre")
       print("6️⃣  Quitter le programme")
       print("-"*50)   
       choix = input("Choix : ")
       if choix == "1":
            display(bibliotéque)
       elif choix == "2":
            add(bibliotéque)
       elif choix == "3":
            delete(bibliotéque)
       elif choix == "4":
           lu(bibliotéque)
       elif choix == "5":
            search(bibliotéque)
       elif choix == "6":
            print("bye see u soon ")
            save(bibliotéque)
            break
       else:
            print("please choose a number between 1 and 6.")

if __name__ == "__main__":
    affichage()
