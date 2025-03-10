# import math
# result = math.sqrt(9)
# print(result)

# # You can import specific function

# from math import sqrt
# result = sqrt(16)
# print(result)

# # You can also import multiple functions or variable at once

# from math import sqrt,pi
# result = sqrt(25)
# print(result)
# print(pi)


# You can also import all functions and variable 

from math import *

result = sqrt(36)
print(result)
print(pi)


# You rename imported module using "as" keyword

import math as m
result = m.sqrt(49)
print(result)
print(m.pi)