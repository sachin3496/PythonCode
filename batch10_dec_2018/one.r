x = as.integer(readline(prompt = "Enter x : "))
y = as.integer(readline(prompt = "Enter y : "))
z = as.integer(readline(prompt = "Enter z : "))

if ( x >= y ) & ( x >= z ) {
  result = x; }
else if ( y >= x ) & ( y >= z ) { 
  result = y; }
else {
  result z;
}

print("The Greatest Number is ")
print(result)
