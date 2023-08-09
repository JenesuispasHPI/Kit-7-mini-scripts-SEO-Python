def generer_balises_meta(titre, description, auteur, date, mots_cles):
    balises_meta = f"""
    <meta charset="UTF-8">
    <title>{titre}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="{auteur}">
    <meta name="date" content="{date}">
    <meta name="keywords" content="{mots_cles}">
    """

    return balises_meta

def main():
    print("Entrez les informations de l'article :")
    titre = input("Titre : ")
    description = input("Description : ")
    auteur = input("Auteur : ")
    date = input("Date : ")
    mots_cles = input("Mots-clés (séparés par des virgules) : ")

    balises = generer_balises_meta(titre, description, auteur, date, mots_cles)
    print("Balises de métadonnées générées :\n", balises)

if __name__ == '__main__':
    main()
