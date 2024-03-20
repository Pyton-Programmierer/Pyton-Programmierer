import random

def roll_dice():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  dice3 = random.randint(1, 6)
  return dice1 + dice2 + dice3

roll_result = roll_dice()
print("Die geworfenen Augenzahlen sind: " + str(roll_result))