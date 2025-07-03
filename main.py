from enigmes import devine_code, message_crypte, fichier_mysterieux, cadenas_logique, epreuve_chrono
from utils import afficher_intro, attendre_entree

def main():
    afficher_intro()

    if not devine_code.jouer():
        return
    attendre_entree()

    if not message_crypte.jouer():
        return
    attendre_entree()

    if not fichier_mysterieux.jouer():
        return
    attendre_entree()

    if not cadenas_logique.jouer():
        return
    attendre_entree()

    if not epreuve_chrono.jouer():
        return
    attendre_entree()

    print("\n🎉 Félicitations ! Vous avez échappé au terminal !")

if __name__ == "__main__":
    main()

