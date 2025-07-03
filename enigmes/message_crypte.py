def jouer():
    print("\n🧩 Énigme 2 : Message crypté")
    message = "Uifsf jt b tfdsfu dpef"
    print(f"Message crypté : {message}")
    reponse = input("Décryptez-le et tapez le message : ")

    return reponse.strip() == "There is a secret code"
