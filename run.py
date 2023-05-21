import random

# Setting Lists for the Deck, The player's Hand, and the Dealer's hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
'J', 'Q', 'K' 'A', 'J', 'Q', 'K' 'A', 'J', 'Q', 'K' 'A','J', 'Q', 'K' 'A',]
playerHand = []
dealerHand = []


def dealCard(turn):
    """
    Deal Card function, selects a random card from the deck, appends it to
    whoever turn it is, and removes this card from the deck
    """
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def calculateTotal(turn):
    """
    This function calculates de total based on what card it is
    """
    total = 0
    letters = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in letters:
            total += 1
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

def revealDealerHand():
    """
    This function reveals the dealer hand when needed, in case a card is added or in case someone wins.
    """
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

