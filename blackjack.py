import random
import sys

print("Welcome to blackjack!")

# Dealer function that gives the dealer their initial hand and draws more if needed
def dealer() -> int:
    dealer_total = random.randint(1, 10) + random.randint(1, 10)
    print(f"Dealer starts with: {dealer_total}")

    # Dealer draws until total reaches at least 17
    while dealer_total < 17:
        new_card = random.randint(1, 10)
        dealer_total += new_card
        print(f"Dealer draws {new_card}. Dealer's total is now {dealer_total}.")
    return dealer_total

# First card the player gets
first_card = random.randint(1, 10)
second_card = random.randint(1, 10)

# Calculate player's initial total
amount = first_card + second_card
print(f"You have {first_card} and {second_card}. Your total is {amount}")

# Dealer's initial draw
dealer_total = dealer()

# Check if dealer gets 21 immediately
if dealer_total == 21:
    print("Dealer hits Blackjack! Dealer wins!")
    sys.exit()

# Check if player gets Blackjack
if amount == 21:
    print("Blackjack! You win!")
    sys.exit()
else:
    choose = input(f'You have {amount}. Would you like to hit or stand? ').lower()

# Player's turn
while choose == 'hit':
    new_card = random.randint(1, 10)
    amount += new_card
    print(f'You drew a {new_card}. Your total is now {amount}.')

    if amount > 21:
        print(f"You bust with a total of {amount}! Dealer wins.")
        sys.exit()
    elif amount == 21:
        print("You win!")
        sys.exit()
    else:
        choose = input(f'Dealer has a hidden total. You have {amount}. Would you like to hit or stand? ').lower()

# Dealer's turn after the player stands
if choose == 'stand':
    print(f'Your final total is {amount}. Dealer\'s final total is {dealer_total}.')

    if dealer_total > 21:
        print("Dealer busts! You win!")
    elif dealer_total > amount:
        print("Dealer wins!")
    elif dealer_total < amount:
        print("You win!")
    else:
        print("It's a tie!")
