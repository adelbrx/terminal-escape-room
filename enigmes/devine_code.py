import random

def jouer():
    print("\n🧩 Énigme 1 : Devine le code")
    code = random.randint(1, 10)
    essais = 3

    while essais > 0:
        try:
            choix = int(input(f"Devine le nombre (1 à 10). Tentatives restantes : {essais} → "))
            if choix == code:
                print("✅ Bravo, c'était le bon code !")
                return True
            else:
                print("❌ Mauvais numéro.")
                essais -= 1
        except ValueError:
            print("⚠️ Entrez un nombre valide.")

    print("🔐 Vous avez échoué...")
    return False
