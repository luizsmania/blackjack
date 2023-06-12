import sys,time,random
from os import system, name
from time import sleep
play = True
#Sets players scores that will be increasing accordingly to wins
dealerScore = 0 
playerScore = 0

def clear():
    """
    Clear fuction for cleaning the terminal
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

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
        elif len(dealerHand) >= 2:
            return dealerHand[0], dealerHand[1]
        
    for _ in range(2): # Give cards to both players
        dealCard(playerHand)
        dealCard(dealerHand)

    while playerIn or dealerIn: # Main game loop, gives card to players and dealer, break if its >= 21
        if len(dealerHand) < 3:
            sprint(f"\nDealer has: {revealDealerHand()} and X")
        else:
            sprint(f"\nDealer has: {revealDealerHand()}, total of {total(dealerHand)} points.\n")
        sprint(f"{user} has: {playerHand}, total of {total(playerHand)} points\n")
        if playerIn:
            stayOrHit = input(f"1 to Stay\n2 to Hit\n")
        if total(dealerHand) > 17:
            sprint("Dealer stays")
            dealerIn = False
        else:
            sprint(f"Dealers hits and gets a new card")
            dealCard(dealerHand)
        if stayOrHit == '1':
            sprint(f"{user} stays")
            playerIn = False
        else:
            sprint(f"{user} hits and gets a new card")
            dealCard(playerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break

    # This if elif statements will check for the total of points in each hand and if someone wins they will stop the game and announce a winner
    if total(playerHand) == 21: 
        sprint(f"\nThe dealer has: {dealerHand}, Total of: {total(dealerHand)} points.\n{user} has: {playerHand}, Total of: {total(playerHand)} points.")
        sprint(f"Blackjack! {user} wins!")
        playerScore+= 1
    elif total(dealerHand) == 21:
        sprint(f"\nThe dealer has: {dealerHand}, Total of: {total(dealerHand)} points.\n{user} has: {playerHand}, Total of: {total(playerHand)} points.")
        sprint(f"Blackjack! Dealer wins!")
        dealerScore+= 1
    elif total(playerHand) > 21:
        sprint(f"\nThe dealer has: {dealerHand}, Total of: {total(dealerHand)} points.\n{user} has: {playerHand}, Total of: {total(playerHand)} points.")
        sprint(f"You bust! Dealer wins!")
        dealerScore+= 1
    elif total(dealerHand) > 21:
        sprint(f"\nThe dealer has: {dealerHand}, Total of: {total(dealerHand)} points.\n{user} has: {playerHand}, Total of: {total(playerHand)} points.")
        sprint(f"Dealer Busts! {user} wins!")
        playerScore+= 1
    elif 21 - total (dealerHand) < 21 - total(playerHand):
        sprint(f"\nThe dealer has: {dealerHand}, Total of: {total(dealerHand)} points.\n{user} has: {playerHand}, Total of: {total(playerHand)} points.")
        sprint(f"Dealer wins")
        dealerScore+= 1
    elif 21 - total (dealerHand) > 21 - total(playerHand):
        sprint(f"\nThe dealer has: {dealerHand}, Total of: {total(dealerHand)} points.\n{user} has: {playerHand}, Total of: {total(playerHand)} points.")
        sprint(f"{user} wins")
        playerScore+= 1
        
    def playAgain():
        global playerScore, dealerScore
        play_again = str(input(f"Would you like to play again? Y/N\n").lower())

        if play_again[0] != "y":
            sleep(1)
            clear()
            sleep(1)
            sprint(f"Alright. Thanks for playing with us! See you again another time.\nFinal Score: {user}: {playerScore}, Dealer: {dealerScore}")
            exit()
        else:
            sleep(1)
            clear()
            sleep(1)
            sprint(f"Alright. A new game is starting.\nScore: {user}: {playerScore}, Dealer: {dealerScore}")
            main()

    playAgain()


sprint("Welcome to Paddy's BlackJack!")
sprint("What is your name, our little winner?")
user = input("")
sprint(f"Would you like to read the rules? Y/N")
readRules = str(input("").lower())
if readRules[0] != "y":
    sprint(f"Alright, It seems that you already know the rules")
else:
    sleep(1)
    clear()
    sleep(1)
    sprint(f"The rules are:")
    sprint(f"Blackjack is played with a conventional deck of 52 playing cards")
    sprint(f"2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.\nFace cards (J,Q,K) count as 10.")
    sprint(f"Ace can count as a 1 or an 11 depending on which value helps the hand the most.")
    sprint(f"The aim of blackjack is to finish the game with a higher total than that of the dealer, without exceeding 21.\nGoing over 21 is commonly known as busting and means an automatic loss.")
    sleep(3)
sprint("Would you like to play a game? Y/N")
playOrNo = str(input("").lower())

if playOrNo[0] != "y":
    sprint(f"Let me know when you are feeling like playing! See ya")
    exit()
else:
    sleep(1)
    clear()
    sleep(1)
    main()
                