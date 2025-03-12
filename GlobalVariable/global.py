x = 10
def my_function():
    global x
    x = 5
    y = 5

my_function()
print(x)
print(y)   #this will cause an error bcz y is a local variable and is not accessible outside of the function