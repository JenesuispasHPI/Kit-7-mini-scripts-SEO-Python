import re

def detecter_verbes_en_ant(texte):
    pattern = r"\b\w+ant\b"
    resultats = re.findall(pattern, texte)
    return resultats

def main():
    print("Entrez votre texte :")
    texte = input()

    resultats = detecter_verbes_en_ant(texte)

    if resultats:
        print("Le texte contient les verbes suivants se terminant par 'ant' :")
        for verbe in resultats:
            print("-", verbe)
    else:
        print("Le texte ne contient pas de verbes en 'ant'.")

if __name__ == '__main__':
    main()
