from donnee import*
import pickle
from random import *


# On vérifie que l'utilisateur existe, et si non on le crée avec un score nul
def check_players(nom) :
    players = {}
    with open("players", "rb") as file :
        unpickler = pickle.Unpickler(file)
        players = unpickler.load()
    user_exists = False
    for cle, score in players.items() :
        if cle == nom :
            user_exists = True
            gameScore = score
    if user_exists == False :
        players[nom] = 0
        with open("players", "wb") as file :
            pickler = pickle.Pickler(file)
            pickler.dump(players)

#On choisit un mot au hasard dans la liste des mots
def choose_mot() :
    index = randrange(7)
    mot = donnee.liste_mots[index]
    return mot


#On masque toutes les lettres du mot nouvellement choisi
def hide_word(word) :
    hidden_word = {}
    for lettre in word :
        hidden_word[lettre] = False
    return hidden_word


#On affiche le mot avec les caractères trouvés par l'utilisateur
def show_hidden_word(hidden_word) :
    show = ""
    for lettre, found in hidden_word.items() :
        if found == True :
            show += lettre
        else :
            show += "*"
    print(show)

#vérifie la saisie des lettres
def input_lettre() :
    lettre = input("Entrez une lettre\n")
    lettre = lettre.lower()
    if len(lettre) > 1 or not lettre.isalpha() :
        print("Erreur: veuillez entrer une lettre\n")
        return input_lettre()
    else :
        return lettre
