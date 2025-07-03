def jouer():
    print("\n🧩 Énigme 3 : Le fichier mystérieux")
    try:
        with open("data/fichier_mystere.txt", "r") as f:
            contenu = f.read()
            print("Contenu du fichier :")
            print(contenu)

        mot_cle = input("Quel est le mot secret caché ? ").strip()
        return "escape" in mot_cle.lower()
    except FileNotFoundError:
        print("⚠️ Fichier non trouvé !")
        return False
