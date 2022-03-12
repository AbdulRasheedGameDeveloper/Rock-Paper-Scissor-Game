#import modules
import random

def Play():
    user = input("your choice? 'r' for 'Rock', 's' for 'Scissor', 'p' for ''Paper' : ")
    computer_AI = random.choice(['r', 's', 'p'])

    if user == computer_AI:
        #Or else print it
        return "It's a Tie Match!!!"
    if is_win(user, computer_AI):
        #This will happen when is_win is true
        return "You've Won!!!"
    #this below return funtion will be called when the computer_AI wins 
    return "You've Lost, Better Luck Next Time!!!"

    
def is_win(player, opponent):
    #Player = r, computer = s: Player Wins
    #Player = s, computer = p: Player Wins
    #Player = p, computer = r: Player Wins

    if((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')):
        return True
        #when the if stament is true the funtion will be true and Player will won the match

#Print the Funtion To Play
print(Play())