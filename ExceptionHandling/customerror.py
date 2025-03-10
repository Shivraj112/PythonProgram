salary = int(input("Enter a salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")