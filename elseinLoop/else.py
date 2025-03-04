# used along with if statement
# with for loop and while loop also
# it appears after the body of the loop
# it will executed after all iteration are completed
# exits loop only after the else block us executed

for x in range(5):
    print("iteration no{} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of loop")