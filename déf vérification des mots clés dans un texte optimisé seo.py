def verifier_mots_cles(titre, sous_titre, description, contenu):
    mots_cles_titre = set(titre.lower().split())
    mots_cles_description = set(description.lower().split())
    mots_cles_contenu = set(contenu.lower().split())

    mots_cles_manquants = mots_cles_titre - mots_cles_description - mots_cles_contenu

    return mots_cles_manquants

def main():
    print("Entrez les informations pour l'article :")
    titre = input("Titre : ")
    sous_titre = input("Sous-titre : ")
    description = input("Description : ")
    contenu = input("Contenu : ")

    mots_cles_manquants = verifier_mots_cles(titre, sous_titre, description, contenu)

    if mots_cles_manquants:
        print("Les mots-clés suivants du titre ne sont pas présents dans la description et le contenu de l'article:")
        for mot_cle in mots_cles_manquants:
            print("-", mot_cle)
    else:
        print("L'article est optimisé pour les mots-clés du titre.")

if __name__ == '__main__':
    main()
