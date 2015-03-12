class Player:

    def __init__(self):
        self.hand_of_cards = []
        self.hand_is_hard = True 

    def take_card(self, card):
        self.hand_of_cards.append(card);

    def hit(self):
        return self.strategy.hit()
    
    def show_hand(self):
        card_string = ""
        for card in self.hand_of_cards:
            card_string += str(card) + "\t"
        return card_string

    def get_score(self):
        score = 0
        ace_array = []
        for card in self.hand_of_cards:
            value = card.get_value()
            if type(value) is str:
                if(value == 'Ace'):
                    ace_array.append(card)
                else:
                    score += 10
            else:
                score += value
        for ace in ace_array:
            if(score < 11):
                score += 11
                self.hand_is_hard = False
            else:
                score += 1
                self.hand_is_hard = True
        return score;
                
            
            
        


