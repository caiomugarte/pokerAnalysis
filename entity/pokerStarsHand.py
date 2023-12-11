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
    
    def serialize_pokerstars_hand(obj):
        if isinstance(obj, PokerStarsHand):
            return {
                "hand_id": obj.hand_id,
                "tournament_id": obj.tournament_id,
                "blind_level": obj.blind_level,
                "is_played": obj.is_played,
                "my_chip_count": obj.my_chip_count,
                "my_position": obj.my_position,
                "battle": obj.battle,
                "my_cards": obj.my_cards,
                "my_blinds": obj.my_blinds,
                "actions": obj.actions
            }
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")