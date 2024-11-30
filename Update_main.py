import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_on_hands):
    if sum(cards_on_hands) == 21 and len(cards_on_hands) == 2:
        return 0
    if 11 in cards_on_hands and sum(cards_on_hands) > 21:
        cards_on_hands.remove(11)
        cards_on_hands.append(1)
    return sum(cards_on_hands)


def compare(u_score, c_score):
    if u_score == c_score:
        return "***Draw***\n"
    elif c_score == 0:
        return "***You lose, computer wins with Black Jack***\n"
    elif u_score == 0:
        return "***You win with Black Jack***\n"
    elif u_score > 21:
        return "***More than 21, you lost***\n"
    elif c_score > 21:
        return "***Computer got more than 21, you win***\n"
    elif u_score > c_score:
        return "****You win****\n"
    else:
        return "****You lose***\n"


restart = True

while restart:
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, score: {user_score}")
        print(f"Computer's first cards {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards {user_cards}, score: {user_score}")
    print(f"Computer's final cards {computer_cards}, score: {computer_score}\n")
    print(compare(user_score, computer_score))

    restart_choice = input("Type 'y' to restart a game, type 'n' to finish: ")
    if restart_choice == 'y':
        print("\n" * 20)
        restart = True
    else:
        restart = False
        print("Thank you for playing!")
