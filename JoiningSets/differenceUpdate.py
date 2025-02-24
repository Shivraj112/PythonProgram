# updates the existing set from another set

cities = {"Haveri","Hubli","Davanagere","Belgavi"}
cities2 = {"Haveri","Harihar","Gadag","Hubli"}
cities.difference_update(cities2)
print(cities)