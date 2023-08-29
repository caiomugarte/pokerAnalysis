from flask import Flask
from analisador import Analisador
from entity.pokerStarsHand import PokerStarsHand
from collections import defaultdict
import os, json

def sort_by_tournament_id(hand):
    return hand.tournament_id


app = Flask(__name__)
path_pokerstars = "pokerfiles/pokerstars"
analisador = Analisador()
tournaments = []

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/api/rest/pokerstars', methods=['GET', 'POST'])
def pokerstars():
    return json.dumps(get_tournaments_info(path_pokerstars, analisador, tournaments), default=PokerStarsHand.serialize_pokerstars_hand, indent=4)

def get_tournaments_info(path, analisador: Analisador, tournaments):
    for file in os.listdir(path):
        tournaments.append(analisador.get_hands(file))
    analisador.montar_estatisticias(tournaments)
    return tournaments

if __name__ == '__main__':
    app.run()