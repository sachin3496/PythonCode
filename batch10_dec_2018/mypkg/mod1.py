"""mod1 module consits two function 
add(a,b) --> print result a+b
pat(n) --> will print normal pattern of n lines 
"""
def add(a,b):
    """add(a,b) --> print a+b"""
    print(f"Result = {a} + {b} = {a+b} ")

def pat(n):
    for var in range(10):
        print("*"*var)


if __name__ == "__main__" : 

    add(4,5)
    pat(10)
