"""
    Blackjack Game
    Developed by Luiz Smania.
    As project for Software Developer course at Code Institute Ireland.
    06/2023
"""

import sys
import time
import random
from os import system, name
from time import sleep

PLAY = True

# Sets players scores that will be increasing accordingly to wins
DEALER_SCORE = 0
PLAYER_SCORE = 0


def generate_deck():
    """
    Generates a deck with 52 cards.
    """
    return [
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K",
        2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"
    ]


deck = generate_deck()


# Setting Lists for the Deck, The player's Hand, and the Dealer's hand

def set_hand():
    """
    Function for emptying player hands when match ends.
    """
    return []


playerHand = set_hand()
dealerHand = set_hand()


def clear():
    """
    Clear fuction for cleaning the terminal
    """
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def sprint(string):
    """
    Function for priting out text slowly
    """
    for character in string + "\n":
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(3.0 / 90)


def deal_card(turn):
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
    face = ["J", "K", "Q"]
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


def reveal_dealer_hand():
    """
    This function reveals the dealer hand when needed,
    in case a card is added or in case someone wins.
    """
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) >= 2:
        return dealerHand[0], dealerHand[1]


def main():
    global PLAYER_SCORE, DEALER_SCORE, playerHand, dealerHand, deck
    # Global variables for when players are playing or not
    playerIn = True
    dealerIn = True

    for _ in range(2):  # Give cards to both players
        deal_card(playerHand)
        deal_card(dealerHand)

    while (playerIn or dealerIn):
        """Main game loop, gives card to players and dealer,
        breaks if it's >= 21"""
        if len(dealerHand) <= 2:
            sprint(f"\nDealer has: {reveal_dealer_hand()} and X")
        else:
            sprint(
                f"\nDealer: {dealerHand}, total: {total(dealerHand)} points.\n"
            )
        sprint(f"{user}: {playerHand}, total of {total(playerHand)} points\n")
        stayOrHit = input("1 to Stay\n2 to Hit\n")
        while stayOrHit not in ["1", "2"]:  # If user hasnt typed either 1 or 2
            sprint("Invalid option. Please choose either 1 or 2.")
            stayOrHit = input("1 to Stay\n2 to Hit\n")

        if total(dealerHand) > 17:
            sprint("Dealer stays")
            dealerIn = False
        else:
            sprint("Dealer hits and gets a new card")
            deal_card(dealerHand)

        if stayOrHit == "1":
            sprint(f"{user} stays")
            playerIn = False
        else:
            sprint(f"{user} hits and gets a new card")
            deal_card(playerHand)

        # Break statements in case someone wins or busts
        if total(playerHand) >= 21:

            break
        elif total(dealerHand) >= 21:
            break

    """This if elif statements will check for the total of points
    in each hand and if someone wins theyll stop the game and announce a winner
    """
    if total(playerHand) == 21:
        sprint(
            f"\nDealer has: {dealerHand}, Total: {total(dealerHand)} points."
        )
        sprint(
            f"{user} has: {playerHand}, Total of: {total(playerHand)} points."
        )
        sprint(f"Blackjack! {user} wins!")
        PLAYER_SCORE += 1
    elif total(dealerHand) == 21:
        sprint(
            f"\nDealer has: {dealerHand}, Total: {total(dealerHand)} points."
        )
        sprint(
            f"{user} has: {playerHand}, Total of: {total(playerHand)} points."
        )
        sprint(f"Blackjack! Dealer wins!")
        DEALER_SCORE += 1
    elif total(playerHand) > 21:
        sprint(
            f"\nDealer has: {dealerHand}, Total: {total(dealerHand)} points."
        )
        sprint(
            f"{user} has: {playerHand}, Total of: {total(playerHand)} points."
        )
        sprint(f"You bust! Dealer wins!")
        DEALER_SCORE += 1
    elif total(dealerHand) > 21:
        sprint(
            f"\nDealer has: {dealerHand}, Total: {total(dealerHand)} points."
        )
        sprint(
            f"{user} has: {playerHand}, Total of: {total(playerHand)} points."
        )
        sprint(f"Dealer Busts! {user} wins!")
        PLAYER_SCORE += 1
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        sprint(
            f"\nDealer has: {dealerHand}, Total: {total(dealerHand)} points."
        )
        sprint(
            f"{user} has: {playerHand}, Total of: {total(playerHand)} points."
        )
        sprint(f"Dealer wins")
        DEALER_SCORE += 1
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        sprint(
            f"\nDealer has: {dealerHand}, Total: {total(dealerHand)} points."
        )
        sprint(
            f"{user} has: {playerHand}, Total of: {total(playerHand)} points."
        )
        sprint(f"{user} wins")
        PLAYER_SCORE += 1

    play_again = str(input(f"Would you like to play again? Y/N\n").lower())

    while (
        True
    ):
        play_again = str(input(f"Would you like to play again? Y/N\n").lower())

        if play_again and play_again[0] == "y":
            sleep(1)
            clear()
            sleep(1)
            sprint(
                f"Alright. A new game is starting."
            )
            sprint(
                f"Score: {user}: {PLAYER_SCORE}, Dealer: {DEALER_SCORE}"
                )
            deck = generate_deck()
            playerHand = set_hand()
            dealerHand = set_hand()
            main()
            
        if play_again and play_again[0] == "n":
            sleep(1)
            clear()
            sleep(1)
            sprint(
                f"Alright. Thanks for playing with us! See you again another time."
            )
            sprint(
                f"Final Score: {user}: {PLAYER_SCORE}, Dealer: {DEALER_SCORE}"
                )
            exit()

        else:
            sprint(
                f"Invalid option. Please choose either Y or N."
            )
        


# Game starting messages
sprint("Welcome to Paddy's BlackJack!")
sprint("What is your name, our little winner?")
user = input("")


while (
    True
):  # Offer the player to read the rules and restarts in case option isnt valid
    sprint("Would you like to read the rules? Y/N")
    readRules = str(input("").lower())

    if readRules and readRules[0] == "y":
        time.sleep(1)
        clear()
        time.sleep(1)
        sprint("The rules are:")
        sprint("Blackjack is played with a conventional")
        sprint("deck of 52 playing cards")
        sprint(
            "2 through 10 count at face value,"
        )
        sprint("i.e. a 2 counts as two, a 9 counts as nine.")
        sprint("Face cards (J,Q,K) count as 10.")
        sprint(
            "Ace can count as a 1 or an 11 depending on"
        )
        sprint("which value helps the hand the most.")
        sprint(
            "The aim of blackjack is to finish the game"
        )
        sprint("with a higher total than that of the dealer,")
        sprint("without exceeding 21.")
        sprint(
            "Going over 21 is commonly known as busting"
        )
        sprint("and means an automatic loss.")
        sleep(3)
        break
    elif readRules and readRules[0] == "n":
        sprint("Alright, it seems that you already know the rules")
        break
    else:
        sprint("Invalid option. Please choose either Y or N.")


while (True):
    """Offer the player to play a game and restarts
    in case option is not valid (Y or N)"""
    playOrNo = input(f"Would you like to play a game? Y/N\n").lower()

    if playOrNo == "y":
        time.sleep(1)
        clear()
        time.sleep(1)
        deck = generate_deck()
        main()
        break
    elif playOrNo == "n":
        sprint("Let me know when you are feeling like playing! See ya")
        break
    else:
        sprint("Invalid option. Please choose either Y or N.")
