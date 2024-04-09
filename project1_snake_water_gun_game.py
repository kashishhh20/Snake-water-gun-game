import random

def game(comp , you):

#if two values are equal, declare a tie!
    if comp == you:
        return None
    
#check for all possibilities when computer chose s:
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True
        
#check for all possibilities when computer chose s:
    elif comp =='w':
        if you =='g':
            return False
        elif you =='s':
            return True
        
#check for all possibilities when computer chose s: 
    elif comp =='g':
        if you =='s':
            return False
        elif you=='w':
            return True


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")

#random number generation between 1-3
randomNo = random.randint(1,3)
if randomNo == 1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==3:
    comp='g'

you = input("Your turn Snake(s) Water(w) or Gun(g)?\n")

a = game (comp,you)

print(f"Computer choose {comp}")
print(f"You chose {you}")

#displaying the result
if a==None:
    print("The game is tie")
elif a:
    print("You win!")
else:
    print("You lose!")