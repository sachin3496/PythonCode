for row in range (7):
    for col in range(7) :
        if (row==3 or col==3) or (col==0 and row>=3) or (row==3 and col<=3) or (col==6 and col>=3) or (row==6 or col<=0):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
   

