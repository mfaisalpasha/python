'''
1.Rock
2.Paper
3.Scissor
'''


q=""
while q != "quit":

    user1=int(input("user1->Enter a choice:"))
    user2=int(input("user2->Enter a choice:"))
    
    if(user1==1) and (user2==2):
                    print("user2 win !")
    elif(user1==1) and (user2==3):
                    print("user1 win !")
    elif(user1==1) and (user2==1):
                    print("Draw game !")
    elif(user1==2) and (user2==1):
                    print("user1 win !")
    elif(user1==2) and (user2==3):
                    print("user2 win !")
    elif(user1==2) and (user2==2):
                    print("Draw game !")
    elif(user1==3) and (user2==1):
                    print("user2 win !")
    elif(user1==3) and (user2==2):
                    print("user1 win !")
    elif(user1==3) and (user2==3):
                    print("Draw game !")
    else:
                    print("Invalid Input !!")
    
    q=input("If you want to quit type 'quit' "
            +"else press a button to continue playing ")
