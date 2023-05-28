import sys,time,random
play = True
dealerScore = 0
playerScore = 0


def sprint(str):
    """
    Function for priting out text slowly
    """
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

def main():
    global playerScore, dealerScore
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
            return dealerHand
        
    for _ in range(2): # Give cards to both players
        dealCard(playerHand)
        dealCard(dealerHand)

    while playerIn or dealerIn: # Main game loop, gives card to players and dealer, break if its >= 21
        sprint(f"\nDealer has: {revealDealerHand()}")
        sprint(f"{user} has: {playerHand}, total of {total(playerHand)} points\n")
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
        sprint(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        sprint(f"Blackjack! {user} wins!")
        playerScore+= 1
    elif total(dealerHand) == 21:
        sprint(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        sprint(f"Blackjack! Dealer wins!")
        dealerScore+= 1
    elif total(playerHand) > 21:
        sprint(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        sprint(f"You bust! Dealer wins!")
        dealerScore+= 1
    elif total(dealerHand) > 21:
        sprint(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        sprint(f"Dealer Busts! {user} wins!")
        playerScore+= 1
    elif 21 - total (dealerHand) < 21 - total(playerHand):
        sprint(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        sprint(f"Dealer wins")
        dealerScore+= 1
    elif 21 - total (dealerHand) > 21 - total(playerHand):
        sprint(f"\n{user} has: {playerHand}, Total of: {total(playerHand)} points. The dealer has: {dealerHand}, Total of: {total(dealerHand)} points")
        sprint(f"{user} wins")
        playerScore+= 1
        
    def playAgain():
        global playerScore, dealerScore
        play_again = str(input("Would you like to play again? Y/N").lower())

        if play_again[0] != "y":
            sprint(f"Alright. Thanks for playing with us! See you again another time.\nFinal Score: {user}: {playerScore}, Dealer: {dealerScore}")
            exit()
        else:
            sprint(f"Alright. A new game is starting.\nScore: {user}: {playerScore}, Dealer: {dealerScore}")
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
            dealerScore = 0
            playerScore = 0
            main()

    playAgain()


sprint("Welcome to Paddy's BlackJack!")
user = input("What is your name, our little winner? ")
playOrNo = str(input("Would you like to play a game? Y/N ").lower())

if playOrNo[0] != "y":
    sprint(f"So get lost")
    exit()
else:
    main()
                