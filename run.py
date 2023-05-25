import random
play = True

print("Welcome to Paddy's BlackJack!")
user = input("What is your name my little winner? : ")
print(f"Alright, {user}, Would you like to play a game? Type Y/N")
while play:
    #Global variables for when players are playing or not
    playerIn = True
    dealerIn = True

    # Setting Lists for the Deck, The player's Hand, and the Dealer's hand
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
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

    def total(turn):
        """
        This function calculates de total based on what card it is
        """
        total = 0
        face = ['J', 'K', 'Q']
        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1 
                else:
                    total += 10
        return total

    def revealDealerHand():
        """
        This function reveals the dealer hand when needed, in case a card is added or in case someone wins.
        """
        if len(dealerHand) == 2:
            return dealerHand[0]
        elif len(dealerHand) > 2:
            return dealerHand[0], dealerHand[1]
        
    for _ in range(2): # Give cards to both players
        dealCard(playerHand)
        dealCard(dealerHand)

    while playerIn or dealerIn: # Main game loop, gives card to players and dealer, break if its >= 21
        print(f"\nDealer has: {revealDealerHand()}\n")
        print(f"{user} has: {playerHand}, total of {total(playerHand)} points\n")
        if playerIn:
            stayOrHit = input(f"1 to Stay\n2 to Hit\n")
        if total(dealerHand) > 17:
            dealerIn = False
        else:
            dealCard(dealerHand)
        if stayOrHit == '1':
            playerIn = False
        else:
            dealCard(playerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break

    # This if elif statements will check for the total of points in each hand and if someone wins they will stop the game and announce a winner
    if total(playerHand) == 21: 
        print(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        print(f"Blackjack! {user} wins!")
    elif total(dealerHand) == 21:
        print(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        print(f"Blackjack! Dealer wins!")
    elif total(playerHand) > 21:
        print(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        print(f"You bust! Dealer wins!")
    elif total(dealerHand) > 21:
        print(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        print(f"Dealer Busts! {user} wins!")
    elif 21 - total (dealerHand) < 21 - total(playerHand):
        print(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        print(f"Dealer wins")
    elif 21 - total (dealerHand) > 21 - total(playerHand):
        print(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        print(f"{user} wins")
    
    play_again = input("Would you like to play again? Y\N").lower()
    if play_again[0] != "y":
        break

                