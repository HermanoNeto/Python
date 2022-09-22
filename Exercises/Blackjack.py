import random
from replit import clear

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def shuffle():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card):
    if 11 in card:
        if sum(card) > 21:
            ace = card.index(11)
            card[ace] = 1
    return sum(card)


def play():

    next = input("Type 'y' to get another card, type 'n' to pass: ")

    if next == "y":
        player_cards.append(shuffle())
        print(f'Your cards: {player_cards}, current score: {calculate_score(player_cards)}')
        if calculate_score(player_cards) > 21:
            print("You Lost")
            return
        return play()
    else:
        print(compare())
        print(f'Your cards: {player_cards}, current score: {calculate_score(player_cards)}')
        print(f'Computer cards: {computer_cards}, Computer score: {calculate_score(computer_cards)}')


def compare():
    user_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 21:
        if computer_score == user_score:
            return "Its a Draw"
        return "You Win"

    if computer_score == user_score:
        return "Its a Draw"

    if computer_score < 21:
        if computer_score > user_score:
            if computer_score < 17:
                computer_cards.append(shuffle())
                return compare()
            return "You Lost\nComputer Wins"

        if computer_score < user_score:
            if computer_score < 17:
                computer_cards.append(shuffle())
                return compare()
            return "You Win"

    if computer_score == 21:
        return "Computer Wins"
        
    if computer_score > 21:
        return "Computer Lose\nYou Win"



player_cards = [shuffle(), shuffle()]
computer_cards = [shuffle(), shuffle()]


while True:
    print(logo)
    play_black = input("Do you want to play a hand of Blackjack? 'y' or 'n'  ")
    clear()

    if play_black == "y":
        player_cards = [shuffle(), shuffle()]
        computer_cards = [shuffle(), shuffle()]
        print(f'Your cards: {player_cards}, current score: {calculate_score(player_cards)}')
        print(f"Computer's first card: {computer_cards[0]}")
        print('-------' * 4)
        play()

    else:
        break
