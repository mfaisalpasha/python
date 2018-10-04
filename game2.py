'''
1.Rock
2.Paper
3.Scissor
'''
def user1():
    number = int(input("user1->Enter a choice:"))
    if (number in range(1,4)):
            print("good choice")
    else:
            print ("You must enter a number between 1-3")
            user1()   
    return number

def user2():
    number2 = int(input("user2->Enter a choice:"))
    if (number2 in range(1,4)):
            print("good choice")
    else:
            print ("You must enter a number between 1-3")
            user2()   
    return number2

q=""
while q != "quit":

    user1=user1()
    user2=user2()
    
    if(user1==1) and (user2==2):
                    print("user2 win !")
    elif(user1==1) and (user2==3):
                    print("user1 win !")
    elif(user1==1) and (user2==1):
                    print("Deaw game !")
    elif(user1==2) and (user2==1):
                    print("user1 win !")
    elif(user1==2) and (user2==3):
                    print("user2 win !")
    elif(user1==2) and (user2==2):
                    print("Deaw game !")
    elif(user1==3) and (user2==1):
                    print("user2 win !")
    elif(user1==3) and (user2==2):
                    print("user1 win !")
    elif(user1==3) and (user2==3):
                    print("Deaw game !")
    else:
                    print("Invalid Input !!")
    
    q=input("If you want to quit type 'quit' "
            +"else press a button to continue playing ")
