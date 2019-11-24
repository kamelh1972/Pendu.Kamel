from fonction import *
import donnee


nom = input("Entrez votre nom:\n")
global gamePlayer
global gameScore

gamePlayer = nom
gameScore = 0
win = False

check_player(nom)
word = choose_word()
hidden_word = hide_word(word)

tentative = donnee.chance;
while tentative > 0 :
    show_hidden_word(hidden_word)
    lettre = input_lettre()
    for key in hidden_word.keys():
        if lettre == key :
            hidden_word[key] = True
    for value in hidden_word.values():
        if value == False :
            continue
        else:
            print("Gagné! Votre score: {}".format(tentative))
            win = True

    tentative -= 1
if win == False :
    print("Perdu! Le mot était {}".format(word))
