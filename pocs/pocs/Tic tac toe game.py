##def tictoetic(user_1,user_2):
##    a=[]
##    b=[]
##    for i in range(0,9):
##        user_1= int(input("ENTER USER1"))
##        a.append(user_1)
##        user_2= int(input("Enter User2"))
##        b.append(user_2)
##        if a[i]==b[i]:
##            print("alredy Entered")
##        print(a)
##        print(b)
##tictoetic(user_1,user_2)
##        

import itertools
a =[]
b =[]
users_list=[]
combinations=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[3,6,9],[2,5,8],[1,5,9],[3,5,7]]
game=True
if len(users_list)==9:
        game=True
        print("game is Tie")
while game:
    sindhu = int(input("sindhu: "))
    while sindhu in users_list:
        sindhu=int(input("Already enter number choose another number"))
    users_list.append(sindhu)
    a.append(sindhu)
    print(a)
    chanse = list(itertools.combinations(a,3))
    if len(a) >=3:
        for i in combinations:
            term = list(itertools.permutations(i))
            for j in term:
                if j in chanse:
                    print("sindhu win")
                    game=False
    
    if game==True:
        rajesh = int(input("rajesh:"))
        while rajesh in users_list:
            rajesh=int(input("Already enter number choose another number"))
        users_list.append(rajesh)
        b.append(rajesh)
        print(b)
        chanse = list(itertools.combinations(b,3))
        if len(b) >=3:
            for i in combinations:
                term = list(itertools.permutations(i))
                for j in term:
                    if j in chanse:
                        print("rajesh win")
                        game=False
    

    


