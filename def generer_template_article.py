def generer_template_article(titre_h1, titre_h2, paragraphes):
    template = f"""
<h1>{titre_h1}</h1>

<h2>{titre_h2}</h2>

"""

    for i, paragraphe in enumerate(paragraphes, 1):
        template += f"<h3>Paragraphe {i}</h3>\n"
        template += f"<p>{paragraphe}</p>\n\n"

    return template

def main():
    print("Entrez les informations pour le template de l'article WordPress :")
    titre_h1 = input("Titre h1 : ")
    titre_h2 = input("Titre h2 : ")

    paragraphes = []
    while True:
        paragraphe = input(f"Paragraphe {len(paragraphes) + 1} (laissez vide pour terminer) : ")
        if not paragraphe:
            break
        paragraphes.append(paragraphe)

    template_article = generer_template_article(titre_h1, titre_h2, paragraphes)
    print("Template de l'article généré :\n", template_article)

if __name__ == '__main__':
    main()
