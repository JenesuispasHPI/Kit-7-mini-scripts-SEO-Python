def main():
    print("Entrez votre méta description d'article :")
    meta_description = input()

    # Vérifie la longueur de la méta description
    meta_description_length = len(meta_description)

    if 100 <= meta_description_length <= 320:
        print("La méta description est optimisée.")
    elif meta_description_length < 100:
        print("La méta description est trop courte.")
    else:
        print("La méta description est trop longue.")

if __name__ == '__main__':
    main()
