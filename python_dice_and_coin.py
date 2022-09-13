'''#this is a comment 
this is a comment too
#flip a coin program
from random import choice, random

#1st method use ramdom,random()

#coin_flip_with_random = "head" if random()> 0.5 else "tails"

#2nd method 
coin_flip_with_choise = choice(["New York","LA","london","Las Vegas","dallas","Florida","Madrid","Dubai"])
print(coin_flip_with_choise)'''
#roll a dice
#1st import to your libaries 
from random import randint
repeat = True
while repeat:
  print("You rolled",randint(1,6))
  print("Do you want to try again")
  repeat  = ("y" or "yes") in input(). lower()
