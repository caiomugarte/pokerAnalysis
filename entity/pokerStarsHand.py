class PokerStarsHand:
    
    def __init__(self, hand_id, tournament_id, blind_level):
        self.hand_id = hand_id
        self.tournament_id = tournament_id
        self.blind_level = blind_level
        self.is_played = None
        self.my_chip_count = None
        self.my_position = None
        self.battle = None
        self.my_cards = None
        self.my_blinds = None
        self.actions = None
    
    def serialize_pokerstars_hand(self):
        if isinstance(self, PokerStarsHand):
            return {
                "hand_id": self.hand_id,
                "tournament_id": self.tournament_id,
                "blind_level": self.blind_level,
                "is_played": self.is_played,
                "my_chip_count": self.my_chip_count,
                "my_position": self.my_position,
                "battle": self.battle,
                "my_cards": self.my_cards,
                "my_blinds": self.my_blinds,
                "actions": self.actions
            }
        raise TypeError(f"Object of type {type(self)} is not JSON serializable")