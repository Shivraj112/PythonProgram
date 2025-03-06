try:
    num = int(input("Enter a integer: "))
except ValueError:
    print("Number is not integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.s")


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)