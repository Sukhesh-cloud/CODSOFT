import string,random
def gen_password():
    length=int(input("Enter length of password required:"))
    ascii_list=Ascii_List()
    password=""
    for i in range(length):
        password+=random.choice(ascii_list)
    print(password)

def Ascii_List():
    ascii_list=string.ascii_letters
    ascii_list+=string.digits
    ascii_list+=string.punctuation
    return ascii_list

if(__name__=="__main__"):
    gen_password()
