def jouer():
    print("\n🧩 Énigme 4 : Cadenas logique")

    paires = {
        "rouge": "feu",
        "bleu": "eau",
        "jaune": "soleil"
    }

    bonnes_reponses = 0
    for couleur, assoc in paires.items():
        r = input(f"À quoi associeriez-vous '{couleur}' ? ").strip().lower()
        if r == assoc:
            bonnes_reponses += 1

    if bonnes_reponses == len(paires):
        print("✅ Toutes les associations sont correctes !")
        return True
    else:
        print(f"❌ Seulement {bonnes_reponses}/{len(paires)} bonnes réponses.")
        return False
