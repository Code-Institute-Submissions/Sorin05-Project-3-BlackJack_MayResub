import random
from art import logo



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




def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
      return "You lose"

    if user_score == computer_score:
      return "Draw" 
    elif computer_score == 0:
      return  "You lose, House has BlackJack"
    elif user_score == 0:
      return "You have BlackJack, YOU WIN"
    elif user_score > 21:
      return "You went over. YOU LOSE"
    elif computer_score > 21:
        return "House went over. YOU WIN"
    elif user_score > computer_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"         


