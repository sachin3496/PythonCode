start = 1
end = 5000

while start <= end : 
    if ( start % 4 == 0 ) and ( start % 100 or start % 400 == 0 ) : 
        print(start,end='\t')
    start += 1
