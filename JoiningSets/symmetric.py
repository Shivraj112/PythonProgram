# prints only items that are not similar to both sets
# it returns new set

cities = {"Haveri","Hubli","Davanageri","Belgavi"}
cities2 = {"Haveri","Harihar","Gadag","Hubli"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)