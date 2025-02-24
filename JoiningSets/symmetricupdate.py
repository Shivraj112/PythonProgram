# it updates the existing set from the anoher set

cities = {"Haveri","Hubli","Davanageri","Belgavi"}
cities2 = {"Haveri","Harihar","Gadag","Hubli"}
cities.symmetric_difference_update(cities2)
print(cities)