f1 = open('bank.db','rb')
f2 = open('bank1.db')
import pickle
import json

d1 = pickle.load(f1)
d2 = json.load(f2)


print("Type of data1 = ",type(d1))
print("Type of data2 = ",type(d2))

print("\nDATA1 = ",d1)
print("\nDATA2 = ",d2)
