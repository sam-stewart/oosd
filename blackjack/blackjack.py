import player
import dealer
import sys
import gamestate
import strategy
from playercheatstrategy import PlayerCheatStrategy
from nostrategy import NoStrategy


bj_dealer = dealer.Dealer()
bj_player = player.Player()

game_state = gamestate.GameState(bj_player, bj_dealer, 
        bj_dealer.deck_of_cards)

bj_player.strategy = PlayerCheatStrategy(game_state)
bj_dealer.strategy = NoStrategy(game_state)

bj_dealer.deal_card(bj_dealer)
bj_dealer.deal_card(bj_dealer)

bj_dealer.deal_card(bj_player)
bj_dealer.deal_card(bj_player)

print("Dealer's hand: \n" + bj_dealer.show_hand_hidden() + "\n")
print("Your hand: \n" + bj_player.show_hand() + "\n")
print("Your score: " + str(bj_player.get_score()))

while raw_input("h to hit or s to stand: ") == 'h':
    bj_dealer.deal_card(bj_player)
    score = bj_player.get_score()
    print("Your hand: \n" + bj_player.show_hand())
    print("Your score: " + str(score) + "\n")
    if score > 21:
        print("You've gone bust")
        sys.exit()

print("Dealer's hand: \n" + bj_dealer.show_hand())

while bj_dealer.get_score() < 17:
    bj_dealer.deal_card(bj_dealer)
    score = bj_dealer.get_score()
    print("Dealer's hand: \n" + bj_dealer.show_hand())
    print("Dealer score: " + str(score) + "\n")
    if score > 21:
        print("Dealer bust!")
        sys.exit()

dealer_score = bj_dealer.get_score()
player_score = bj_player.get_score()

print("**********")
print("Your score: "  + str(player_score))
print("Dealer score: " + str(dealer_score) + "\n")

if dealer_score < player_score:
    print("You win")
elif dealer_score > player_score:
    print("Dealer wins")
else:
    print("Draw")







