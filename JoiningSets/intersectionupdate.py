# it updates the existing set from another set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)


cities = {"Haveri","Hubli","Davanagere","Belgavi"}
cities2 = {"Haveri","Harihar","Gadag","Hubli"}
cities.intersection_update(cities2)
print(cities)