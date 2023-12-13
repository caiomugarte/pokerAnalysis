from flask import Flask, jsonify
from analisador import Analisador
from entity.pokerStarsHand import PokerStarsHand
from collections import defaultdict
import os, json

def sort_by_tournament_id(hand):
    return hand.tournament_id


app = Flask(__name__)
path_pokerstars = "pokerfiles/pokerstars"
analisador = Analisador()

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/api/rest/pokerstars', methods=['GET', 'POST'])
def pokerstars():
    torneios = get_tournaments_info(path_pokerstars, analisador)
    return jsonify({"torneios": torneios})

def get_tournaments_info(path, analisador: Analisador):
    torneios = []
    for file in os.listdir(path):
        hands = analisador.get_hands(file)
        torneio = [];
        for hand in hands: 
            torneio.append(hand.serialize_pokerstars_hand())
        torneios.append({'torneio': hands[0].tournament_id, "hands": torneio})
    return torneios

if __name__ == '__main__':
    app.run()