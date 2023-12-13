
from entity.pokerStarsHand import PokerStarsHand
from collections import defaultdict
import re

POSITIONS = ["BTN", "SB", "BB", "UTG", "UTG+1", "MP", "LJ", "HJ", "CO"]

class Analisador: 
    def get_hands(self, file):
        hands_details = get_detalhes_maos(file)
        hands = []
        fill_hands(hands_details, hands)
        return hands
    
def fill_hands(hands_details, hands):
    for hand in hands_details:
        lines = hand.split('\n')
        hand_info = lines[0]

        hand_id = get_hand_id(hand_info)
        tournament_id = get_tournament_id(hand_info)
        blind_level = get_blind_level(hand_info)

        hand = PokerStarsHand(hand_id, tournament_id, blind_level)
        hand.description = lines
        hand.is_played = get_is_played(lines)
        hand.my_chip_count = get_chip_count(lines)

        hand.my_blinds = get_my_blinds(hand)

        hand.my_position = get_position(lines, "Caio Mugarte")
        hand.battle = get_battle(lines)
        
        trata_battle(hand)

        hand.my_cards = get_my_cards(lines)
        hand.result = get_result(lines)

        hand.actions = get_actions(lines)

        hands.append(hand)

def get_actions(lines):
    actions = []
    preflop_started = False  # Flag para indicar se o preflop começou

    for line in lines:
        # Verifica se o flop começou
        if "*** FLOP ***" in line:
            preflop_started = False

        # Verifica se a linha contém informações sobre as ações dos jogadores
        if preflop_started and re.match(r'^[A-Za-z0-9\s]+: (posts|folds|calls|raises|bets|checks|shows)', line):
            actions.append(line.strip())

        # Verifica se o preflop começou
        if "*** HOLE CARDS ***" in line:
            preflop_started = True

    return actions

def get_my_blinds(hand: PokerStarsHand):
    bb = int(hand.blind_level.split('/')[1][:-1])
    return int(hand.my_chip_count) / bb
    
        
def get_result(lines):
    collected = []
    for line in lines:
        if "collected" in line:
            collected.append(line)
def trata_battle(hand):
    if hand.battle=="":
        hand.battle = hand.my_position

def is_line_a_hand(line):
    return "Hand" in line

def trata_lista_maos(hands):
    hands_filtered = list(filter(None, hands))
    return hands_filtered

def get_blind_level(hand_info):
    blind_level_match = re.search(r'Level (\w+) \((\d+)/(\d+)\)', hand_info)
    return f"({blind_level_match.group(2)}/{blind_level_match.group(3)})"

def get_detalhes_maos(file): 
    with open('pokerfiles/pokerstars/' + file, 'r') as file:
        lines = file.readlines()
        hands = []
        hand_line = ''
        for line in lines:
            if(is_line_a_hand(line)):
                hand_line += line
            elif ("\n" != line):
                hand_line += line
            else:
                hands.append(hand_line)
                hand_line = ''
    return trata_lista_maos(hands)

def get_chip_count(lines):
    for line in lines:
        if "in chips" in line and "Caio Mugarte" in line:
            pattern = r"(\d+) in chips"
            return re.search(pattern, line).group(1)
    
def get_is_played(lines):
    for line in lines:
        if "Caio Mugarte: folds" in line:
            return False
    return True

def get_position(lines, player):
    player_seats = {}
    botao = None

    for line in lines:
        if " is the button" in line:
            botao = int(re.search(r"Seat #(\d+)", line).group(1))

        player_match = re.search(r"Seat (\d+): ([^(]+) \((\d+) in chips\)", line)
        if player_match:
            seat_number = int(player_match.group(1))
            name = player_match.group(2).strip()
            player_seats[seat_number] = name

    seat = next((seat for seat, name in player_seats.items() if player in name), None)
    return POSITIONS[(9+ seat - botao)%9] 

def get_hand_id(hand_info):
    return re.search(r'#(\d+):', hand_info).group(1)

def get_tournament_id(hand_info):
    return re.search(r'Tournament #(\d+),', hand_info).group(1)

def get_battle(lines):
    involved_seats = set()
    battle_str = ""

    for line in lines:
        if "bets" in line or "calls" in line or "raises" in line:
            parts = line.split(":")
            if len(parts) > 0:
                seat_info = parts[0].strip()
                involved_seats.add(seat_info)

    for index, player in enumerate(involved_seats):
        battle_str += get_position(lines, player)

        if index < len(involved_seats) - 1:
            battle_str += " vs "

    return battle_str

def get_my_cards(lines):
    for line in lines:
        if "Dealt to Caio Mugarte" in line:
            match = re.match(r"Dealt to Caio Mugarte \[(\w{2}) (\w{2})\]", line)
    return match.group(1) + ":" + match.group(2)