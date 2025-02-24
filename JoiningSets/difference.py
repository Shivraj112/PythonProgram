# prints only items that are only present in original set and  not in both sets
# it returns the new set

cities = {"Haveri","Hubli","Davanagere","Belgavi"}
cities2 = {"Haveri","Harihar","Gadag","Hubli"}
cities3 = cities.difference(cities2)
print(cities3)