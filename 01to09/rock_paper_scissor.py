import random
def play():
    user= input(" Whats your choice'r' for ROCK 'p' for PAPER and 's' for SCISSOR: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
     return "tie"
    
    if is_win(user,computer):
       return 'you won'
    
    return 'you lost'


def is_win(player,opponent):
       if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
       or (player == 'p' and opponent == 'r'):
          
          return True
print (play() )    