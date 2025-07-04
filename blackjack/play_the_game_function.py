import random
def play_the_game():
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,11]
    user = []
    dealer = []
    i = 0
    while i < 2:
        dealer.append(random.choice(cards))
        user.append(random.choice(cards))
        i += 1
    print(user , dealer)   
    def total_value():
        user_total_score = sum(user)
        dealer_total_score = sum(dealer)
        if 11 in user and sum(user) > 21:
            user.remove(11)
            user.append(1)
        print(f"Users total score is {user_total_score}. And the dealer total score is {dealer_total_score}")
        return user_total_score , dealer_total_score
    def compare_scores(user_total_score, dealer_total_score):
        if user_total_score > 21:
            return "User busts. You lose."
        elif dealer_total_score > 21:
            return "Dealer busts. You win."
        elif user_total_score > dealer_total_score:
            return "User wins!"
        elif dealer_total_score > user_total_score:
            return "Dealer wins."
        else:
            return "It's a draw."
    while True:
        user_wants_to_draw = input("Want to draw another card? y/n? ")
        if user_wants_to_draw == "y":
            user.append(random.choice(cards))
            if 11 in user and sum(user) > 21:
                user.remove(11)
                user.append(1)
            user_score, dealer_score = total_value()
            print(f"User total score is {user_score}")
            if user_score > 21:
                print("Bust. You lose")
                break
        elif user_wants_to_draw == "n":
            while sum(dealer) < 17:
                new_card = random.choice(cards)
                dealer.append(new_card)
                print(f"Dealer draws: {new_card}")
                if sum(dealer) > 21 and 11 in dealer:
                    dealer.remove(11)
                    dealer.append(1)
            print(f"Dealer's final hand: {dealer} -> total: {sum(dealer)}")
            print(f"User's final hand: {user} -> total: {sum(user)}")
            print(compare_scores(sum(user), sum(dealer)))
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")