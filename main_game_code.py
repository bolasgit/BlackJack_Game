import os
import random
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return (card)

def calculate_score(cards_dealt):
  if sum(cards_dealt) == 21 and len(cards_dealt) == 2:
    return 0 
  return sum(cards_dealt)
  if 11 in cards_dealt and sum(cards_dealt) > 21:
    cards_dealt.remove(11)
    cards_dealt.append(1)
#step5

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "  Its a draw"
  elif computer_score == 0:
    return "  I am sorry, you lose"
  elif user_score == 0:
    return "  BLACKJACK!! You win"
  elif user_score > 21:
    return "  I am sorry, you lose"
  elif computer_score > 21:
    return "  You win!"
  elif user_score > computer_score:
    return "  You win!"
  else:
    return "  I am sorry, you lose"

def lets_play():
  endgame = False
  print(logo)
  print("Welcome to Bola's BlackJack game.")
  name = input("What is your name? ")
  user_cards = []
  computer_cards = []
  
  # for i in range(2):
  #   new_card = deal_card()
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())
  
  
  while not endgame:
    # print(f"{name}'s deal : {user_cards}")
    # print(f"computer's deal : {computer_cards[0]}")
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print (f"  {name}'s total : {user_score}")
    print (f"  computer's total : {computer_score}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      endgame = True
    else:
      redeal = input("  Will you like to pick another card? 'y' or 'n' ")
      if redeal == 'y':
        user_cards.append(deal_card())
      else:
        endgame = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print (f" computer score : {computer_score}")
  print (f" computer cards : {computer_cards}")
  print (f" {name}'s' score : {user_score}")
  print (f" {name}'s' cards : {user_cards}")
  print (compare(user_score, computer_score))

while input("  Do you want to play a game of Blackjack? 'y or 'n ") == 'y':
  
#   clear() use this if you define a function to clear screen
  os.system('clear')
  lets_play()
      
