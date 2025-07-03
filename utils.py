
def afficher_intro():
    print("🔒 Vous êtes piégé dans un terminal...")
    print("🧠 Résolvez les énigmes pour vous échapper.\n")

def attendre_entree():
    input("\nAppuyez sur Entrée pour continuer...")

def verifier_reponse(utilisateur, attendu):
    return utilisateur.strip().lower() == attendu.lower()
