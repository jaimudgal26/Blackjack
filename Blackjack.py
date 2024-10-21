import random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(u_Score, c_Score):
  if u_Score == c_Score:
    return "draw"
  elif c_Score == 0:
    return "Lose, opponent has Blackjack"
  elif u_Score == 0:
    return "Win with a Blackjack"
  elif u_Score > 21:
    return "You went over. You lose"
  elif c_Score > 21:
    return "Opponent went over. You win"
  elif u_Score > c_Score:
    return "You win"
  else:
    return "You lose"


user_cards = []
computer_cards = []
is_game_over = False

for fillingCards in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
while not is_game_over:

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card : {computer_cards[0]}")

  if user_score == 0 or user_score > 21:
    is_game_over = True
  else:
    user_should_deal = input(
        "Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
      user_cards.append(deal_card())
    else:
      is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))
