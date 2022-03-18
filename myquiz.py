print(" Welcome To Drew's Quiz Game \n You Probably Won't Win!")
Player = input(" Do You Want To Try My Quiz? \n" )
if Player.lower() != 'yes':
    print("Good Bye, You Failed!")
    quit()  

name_player = input("Enter Your Name For The Quiz: ")

print("Let's See What You Got :) ",name_player)

score = 0

answer = input(' What does CPU stand for? \n ')
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' What does GPU stand for? \n ')
if answer.lower() == 'graphical processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does RAM stand for? \n ')
if answer.lower() == 'random access memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does ROM stand for? \n ')
if answer.lower() == 'read only memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Who is the coolest guy ever? \n ')
if answer.lower() == 'drew':
    print("Correct")
    score += 1
else:
    print('You Wrong! It is Drew')
    
print("You got " + str(score)+ " correct answers")
print("You got " + str((score/5) *100)+ " %")
