import donnee
import pickle
from random import randrange


# On vérifie que l'utilisateur existe, et si non on le crée avec un score nul
def check_player(nom) :
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
