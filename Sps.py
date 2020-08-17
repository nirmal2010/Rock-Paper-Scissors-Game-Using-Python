import random

def computer():
    comp=random.choice(['scissor','stone','paper'])
    return comp
def user():
    choose=input("Enter stone, paper or scissor to play:").lower()
    return choose
limit=int(input("Enter the final score to be taken to win:")) 
c=0
p=0
while True:
    choose=user()
    com=computer()
    print("Computer puts {}".format(com))
    if choose==com:
        print("Result: Draw")
    elif choose == 'scissor':
        if com == 'paper':
            print("You win")
            p+=1
        elif com == 'stone':
            print("Computer wins")
            c+=1
    elif choose == 'stone':
        if com == 'scissor':
            print("You win")
            p+=1
        elif com == 'paper':
            print("Computer wins")
            c+=1
    elif choose == 'paper':
        if com == 'stone':
            print("You win")
            p+=1
        elif com == 'scissor':
            print("Computer wins")
            c+=1
    else:
        print("Invalid input Check spelling and try again")
    print("Your point {}".format(p))
    print("Computer point {}".format(c))
    

    if p==limit:
        print("Congratulation you have won")
        break
    if c==limit:
        print("Oops! better luck next time")
        break
#limit=int(input("Enter the final score to be taken to win:"))
#gameplay(limit)

