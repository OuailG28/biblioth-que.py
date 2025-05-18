import requests
import json
import csv

def getContacts(api_key, query):
    """
    Exécuter GET pour appeler la méthode mapssearch de ScraperAPI
    save les informations dans un JSON
    """
    SCRAPERAPI_URL = f"https://api.scraperapi.com/structured/google/mapssearch?api_key={api_key}&query={query}"

    try:
        response = requests.get(SCRAPERAPI_URL)
        response.raise_for_status()  # Vérifie si la requête a réussi

        with open("contacts.json", "w", encoding="utf-8") as json_file: 
            json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

        print("Données enregistrées dans contacts.json")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
    
def traitementData():
    """
    Récupérer la liste des contacts avec les informations utiles.
    """
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        results = []
        
        if "results" not in data:
            print("Aucune donnée trouvée.")
            return results

        for b in data["results"]:
            nom = b.get("name", "Vide").replace(",", "")  
            adress = b.get("address", ["Vide"])  

            # Vérifier si l'adresse contient assez d'éléments
            adresse_complete = " - ".join(adress) if isinstance(adress, list) else adress

            c = {
                "Nom": nom,
                "URL": b.get("url", "Vide"),
                "Addresse": adresse_complete,
                "NombreEtoile": b.get("stars", 0),
                "NombreReview": b.get("ratings", 0),
                "Type": ", ".join(b.get("type", ["Vide"]))
            }
            results.append(c)

        with open("contactsFinaux.json", "w", encoding="utf-8") as json_file: 
            json.dump(results, json_file, ensure_ascii=False, indent=4)

        print("Données traitées et enregistrées dans contactsFinaux.json")
        return results

    except Exception as e:
        print(f"Erreur dans traitementData : {e}")
        return []

def filterNombreEtoile(entreprises, etoile=1):
    """
    Filtrer les entreprises par nombre d'étoiles et save en CSV.
    """
    goal = [e for e in entreprises if e["NombreEtoile"] >= etoile]

    try:
        with open("contactsFinaux.csv", "w", newline="", encoding="utf-8") as csv_file:
            champ = ["Nom", "URL", "Addresse", "NombreEtoile", "NombreReview", "Type"]
            ecr = csv.DictWriter(csv_file, fieldnames=champ)
            ecr.writeheader()
            ecr.writerows(goal)

        print(f"dossier CSV contactsFinaux.csv généré avec {len(goal)} résultats.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde CSV : {e}")

if __name__ == "__main__":
    # API_KEY = "" input("Entrez votre clé API ScraperAPI : ").strip()
    API_KEY = "9b43563fb65212851488db30022f7088"
    QUERY = input("Que voulez-vous chercher : ")

    if not API_KEY:
        print("Erreur : Veuillez entrer une clé API valide.")
    else:
        getContacts(API_KEY, QUERY)
        results = traitementData()
        filterNombreEtoile(results, 4)  
