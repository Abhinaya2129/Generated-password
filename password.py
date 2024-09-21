import random

alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=(0,1,2,3,4,5,6,7,8,9)
sym=['!','@','#','$','%','^','&','*','~','?']
pwd=[]

def password():
    length = int(input("give the length of the password : "))
    if length < 8:
        print("password length must be above 8.......!") 
        password()
    elif length > 8:
        for i in range(length-4):
            ran_alp = random.choice(alp)
            pwd.append(ran_alp)
        for i in range(1):
            ran_sym = random.choice(sym)
            pwd.append(ran_sym)
        for i in range(3):
            ran_num = random.choice(num)
            pwd.append(ran_num)
        for i in pwd:
            print(i,end="")
#print(pwd)
password()



