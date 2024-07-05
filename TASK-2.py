def main():
    choice=int(input("1.Addition\
                \n2.Subtraction\
                \n3.Multiplication\
                \n4.Division\
                \n5.Modulo\
                \n6.Exponent\nEnter choice:"))
    if(choice==1):
        a,b=map(int,input("Enter 2 No's:").split())
        result=a+b
        print("Answer is:"+str(result))
    if(choice==2):
        a,b=map(int,input("Enter 2 No's:").split())
        result=a-b
        print("Answer is:"+str(result))
    if(choice==3):
        a,b=map(int,input("Enter 2 No's:").split())
        result=a*b
        print("Answer is:"+str(result))
    if(choice==4):
        a,b=map(int,input("Enter Num/Den:").split('/'))
        result=a+b
        print("Answer is:"+str(result))
    if(choice==5):
        a,b=map(int,input("Enter Num%Den:").split('%'))
        result=a%b
        print("Answer is:"+str(result))
    if(choice==6):
        a,b=map(int,input("Enter base and exp:").split())
        result=a**b
        print("Answer is:"+str(result))

if(__name__=="__main__"):
    while(True):
        main()
        
    
                 
    
