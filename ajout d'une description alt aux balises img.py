import re

def ajouter_alt_aux_images(texte):
    def remplacer_balise_img(match):
        balise_img = match.group(0)
        if 'alt=' not in balise_img:
            balise_img_modifiee = balise_img[:-1] + ' alt="Description de l\'image"' + balise_img[-1]
            return balise_img_modifiee
        return balise_img

    pattern = r"<img[^>]*>"
    texte_modifie = re.sub(pattern, remplacer_balise_img, texte)

    return texte_modifie

def main():
    print("Entrez votre texte avec les balises <img> :")
    texte = input()

    texte_modifie = ajouter_alt_aux_images(texte)
    print("Texte modifié :\n", texte_modifie)

if __name__ == '__main__':
    main()
