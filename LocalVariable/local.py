x = 10              #global variable
def my_function():
    y = 5           #Local Variable
    print(y)

my_function()
print(x)
print(y) # this cause error bcz variable y is local variable so it's not accessed outside of the function