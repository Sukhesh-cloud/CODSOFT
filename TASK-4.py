import random
def game(user_score,comp_score):
    user_choice=input("Enter rock or paper or scissor:")
    user_choice=user_choice.lower()
    list=['rock','paper','scissor']
    computer_choice=random.choice(list)
    print("Computer Choice is:"+computer_choice)
    if(user_choice==computer_choice):
        print("Match Draw!!!")
    elif(user_choice=="rock" and computer_choice=="scissor"):
        print("You Won...")
        user_score+=1
    elif(user_choice=="scissor" and computer_choice=="paper"):
        print("You Won...")
        user_score+=1
    elif(user_choice=="paper" and computer_choice=="rock"):
        print("You Won...")
        user_score+=1
    else:
        print("Computer Won")
        comp_score+=1
    return user_score,comp_score
    

if(__name__=="__main__"):
    ch='cont'
    user_score,comp_score=0,0
    while ch=='cont':
        user_score,comp_score=game(user_score,comp_score)
        ch=input("Enter cont/exit")
        if(ch=='exit'):
            if(user_score>comp_score):
                print(f"You Won and score is {user_score} points")
            else:
                print(f"Computer Won and score is {comp_score} points")

