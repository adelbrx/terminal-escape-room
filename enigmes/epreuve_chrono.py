import time

def jouer():
    print("\n🧩 Énigme 5 : Épreuve chronométrée")
    print("Vous avez 10 secondes pour taper : terminal_escape")

    start = time.time()
    reponse = input("Tapez maintenant ! → ")
    end = time.time()

    if reponse.strip() == "terminal_escape" and end - start <= 10:
        print("✅ Réussi dans les temps !")
        return True
    else:
        print("⏱️ Trop lent ou mauvaise réponse.")
        return False
