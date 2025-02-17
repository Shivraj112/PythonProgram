names = ["Shiva","Mahadeva","Shambho","Bhairava","Mahakal"]
namesWith_O = [items for items in names if "o" in items]
print(namesWith_O)

# More than 4 letters

namesWith_4 = [items for items in names if(len(items) > 4)]
print(namesWith_4)