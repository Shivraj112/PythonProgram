# applePrice = 210
# budget = 200
# if (applePrice <= budget):
#     print("You can buy apple")
# else:
#     print("You can't buy appale ")


# age = int(input("Enter Your age: "))



# if (age > 18):
#     print("You can vote")
# else:
#     print("You can't Vote")


number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))
if (number1 <= number2 and number1 <= number3):
    print(f'The smallest number is {number1}')
elif (number2 <= number1 and number2 <= number3):
    print(f"The smallest number is {number2}")
else:
    print(f"The smallest number is {number3}")