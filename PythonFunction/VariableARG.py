#variable length argument

# 1) Arbitary argument - pass * before the parameter

def name (*name):
    print("Hello", name[0],name[1],name[2])
name("Shiva","Bhairava","Adiyogi")

# 2) Keyword Arbitary argument - pass ** before the parameter

def name (**name):
    print("Namaste",name["fname"],name["mname"],name["lname"])
name(mname = "Shiva", lname = "Bhairava", fname = "Mahakal")