datafile = input('sourcefile : ')
file = open(datafile)
data = file.read()
file.close()
d = data.split('\n')

new_data = []
for item in d :
    new_data.append(item.split(','))
from getpass import getpass

def valid():
    p = getpass("Password : ")
    p1 = getpass("Confirm Password : ")
    if p == p1 : 
        return p
    return valid()

username = input("Username : ").strip().lower()
for item in new_data : 
    if item[0].strip().lower() == username: 
        item[2] = valid()
new_data1 = []
for item in new_data : 
    new_data1.append(','.join(item))
result = '\n'.join(new_data1)

f = open(datafile,'w')
f.write(result)
f.close()
