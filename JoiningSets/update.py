# adds into the existing set from another set

cities = {"Haveri","Hubli","Davanageri","Belgavi"}
cities2 = {"Haveri","Harihar","Gadag","Hubli"}
cities.update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)