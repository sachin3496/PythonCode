def swastik(n_rows):

    if n_rows % 2 : 
        pass
    else :
        n_rows += 1

    mid_point = ( n_rows // 2 ) + 1

    for row in range(1,n_rows+1):
        if row == 1 : 
            print("*"," "*(n_rows//2-1),"*"*(n_rows//2+1),sep='')
        elif row < mid_point : 
            print("*"," "*(mid_point-2),"*",sep='')
        elif row == mid_point : 
            print("*"*(n_rows),sep='')
        elif row < n_rows : 
            print(" "*(mid_point-1),"*"," "*(mid_point-2),"*",sep='')
        else : 
            print("*"*mid_point," "*(mid_point-2),"*",sep='')

if __name__ == "__main__" : 

    print("File __name__ == ",__name__)
    swastik(int(input("Enter number of lines : ")))
