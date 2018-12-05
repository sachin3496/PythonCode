
from random import randint

l = [ randint(1,50) for var in range(20 )]
print(*l)

k = [ 0 if num % 2 else 1 for num in l ]
s = ''
for var in k :
    s = s+'\t'+str(var)

print(s)
