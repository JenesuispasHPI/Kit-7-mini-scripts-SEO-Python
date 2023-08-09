def main():
    print("Entrez un titre optimisé entre 10 et 60 caractères :")
    title = input()

    # Vérifie la longueur du titre
    title_length = len(title)

    if 10 <= title_length <= 60:
        print("Le titre est optimisé.")
    elif title_length < 10:
        print("Le titre est trop court.")
    else:
        print("Le titre est trop long.")

if __name__ == '__main__':
    main()
