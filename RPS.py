rock = '''
      Rock  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
      Paper
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
     scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
r = rock
s = scissors
p = paper

import random

def rps():
      # number of lives
      life = 5
      keep_playing = True
      print(f'You have received {life} lives for this gamep')
      while life > 0 and keep_playing == True:      
            # generate player and computer choice
            player_input = input('Enter r, p, s for Rock, Paper, Scissors:')
            game_list = ['r','p','s']
            computer_input = random.choice(game_list)
            # convert input to Ascil Art variable
            if player_input == 'r' or player_input == 'p' or player_input == 's':
                  print('You chose:')
                  if player_input == "r":
                        print(r)
                  elif player_input == "s":
                        print(s)
                  else:
                        print(p)
                  print('Computer chose:')        
                  if computer_input == "r":
                        print(r)
                  elif computer_input == "s":
                        print(s)
                  else:
                        print(p) 

                        #Logical functions for the game 
                  if player_input == computer_input:
                        print('a tie!')
                  elif player_input == 'r':
                        if computer_input == 's':
                              print('Rock Smashes Scissors, You Win!')
                        else:
                              print('Paper Covers Rock, You Lose!')
                              life -= 1
                              print(f'You have {life} more lives')
                  elif player_input == 'p':
                        if computer_input == 's':
                              print('Scissors Cuts Paper, You Lose!')
                              life -= 1
                              print(f'You have {life} more lives')
                        else:
                              print ('Paper Covers Rock, You Win!')
                  else:
                        if computer_input == 'p':
                              print('Scissors Cuts Paper, You Win!')
                        else:
                              print('Rock Smashes Scissors, You Lose!')
                              life -= 1
                              print(f'You have {life} more lives')         
            else:            
                  print("You lose!, invalid selection")
                  life -= 1
                  print(f'You have {life} more lives')
            choice = input('Would you like to keep playing? : [y/n]')
            if choice == 'y':
                  keep_playing = True
            else:
                  keep_playing = False 
rps()



