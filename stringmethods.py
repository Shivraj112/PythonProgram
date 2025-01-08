# upper() every letters in string converts to upper case

# a="shivaraj"
# print(a.upper())  #print(upper(a)) / print(a.upper(a)) this is code is wrong 

#mahadeva,mahakal,bhairava,kaali,basavanna,huligemma,raghevendra


# a="mahadeva"
# print(a.upper())

# mh="MahaKal"
# print(mh.upper())

# bh="bhairava"
# print(bh.upper())

# ka="kaali"
# print(ka.upper())

# basav="basavanna"
# print(basav.upper())

# huli="huligemma"
# print(huli.upper())

# rg="raghavendra"
# print(rg.upper())

# sg="sadhguru"  # NO SEMI-COLON OR COLON IN PYTHON
# print(sg.upper())

#/////////////////////////////////////////////////////////////////////////////////

#lower()

#shivaraj,raghavendra,mahadeva,mahakal,bhairava,kaali,basava,huligemma

# sh="SHIvARAJ"
# print(sh.lower())

# rg="RAGHAVENDRA"
# print(rg.lower())

# mh="MAHADEVA"
# print(mh.lower())

# md="MahadeVA"
# print(md.lower())

# mk="Mahakal"
# print(mk.lower())

# bh="BAIRAva"                 #NO SEMICOLON
# print(bh.lower())

# kl="KAALI"
# print(kl.lower())

# bs="BASAVANNA"
# print(bs.lower())

# hl="hULIGEMMA"
# print(hl.lower())


#//////////////////////////////////////////////////////////////////////////////////

#  strip()  removes white space before and after the string

#raghavendra basavanna huligemma mahadeva bhairava kaali shivraj

# rg="   raghavendra     "
# print(rg.strip())

# rd="   raghavendra   "
# print(rd)

# bs="       basavanna    "
# print(bs.strip())

# huli="  huligemma   "
# print(huli.strip())

# mh="    maha    deva   "    #it will only remove before and after of string
# print(mh.strip())

# bh="    bhairava    "
# print(bh.strip())

# kl="    kaali   "
# print(kl.strip())

# sh="    shivraj     "
# print(sh.strip())

#///////////////////////////////////////////////////////////////////////////////////////

#rstrip()  it remove unwanted symbols at last not at the beginning

#raghavendra basavanna huligemma mahadeva bhairava kaali shivraj

# rg="raghavendra!!!@@"
# print(rg.rstrip("!@"))  #   print(rg.rstrip("!","@")) we shoud not use like this to remove two symbols 

# basav="basavanna@!#"
# print(basav.rstrip("@!#"))

# huli="huligemma###$%"
# print(huli.rstrip("#$%"))

# mh="mahadeva!@#"
# print(mh.rstrip("!@#"))

# bh="bhairava*&^" #no semi colon no ;;;;;;
# print(bh.rstrip("*&^"))

# ka="kaali%^"
# print(ka.rstrip("%^"))

# sh="shivaraj%^"
# print(sh.rstrip("%^"))

# sd="!!!mahadeva"   #it will only remove at last 
# print(sd.rstrip("!"))

#/////////////////////////////////////////////////////////////////////////////////////////////

#replace() 

#raghavendra->rayaru,basavanna->nandi,huligemma->hulige,mahadeva->devaraj,bhairav->bhaira,

# "om namaha shivaya -> aum"

# rg="raghavendra"
# print(rg.replace("ragha","raya"))

# om="om namah shivaya"
# print(om.replace("om","aum"))

# basav="basavanna"
# print(basav.replace("basavanna","nandi"))

# huli="huligemma"
# print(huli.replace("huligemma","amma"))

# mh="mahadeva"
# print(mh.replace("deva","raj"))

# bh="bhairava"
# print(bh.replace("bhairava","maha bhairava"))

# md="mahadevi"
# print(md.replace("devi","deva"))

#//////////////////////////////////////////////////////////////////////////////

#split()   output as list [ashcvhgs,dgaa,gdhg]

# str="Silver Spoon"
# print(str.split(" "))

# str1="Silver@Spoon"
# print(str1.split("@"))

# rg="raghavendra@mantralaya"
# print(rg.split("@"))

# bs="basav anna har har mahadeva"
# print(bs.split(" "))

# hl="udho@udho@huligemma"
# print(hl.split("@"))

# mh="mahadeva shanbho"
# print(mh.split(" "))

# bh="bhairava%namaha"
# print(bh.split("%"))

# mk="mahakal namaha"
# print(mk.split(" "))  #yav word split agbeku annodanna double/single inverted comma hakbeku

# ka="Maha@kali"
# print(ka.split("@"))

# sh="shambho mahadeva"
# print(sh.split(' ')) #used single

#/////////////////////////////////////////////////////////////////////////////////////

#capitalize() first letter capitalizes

#raghavendra,basavanna,huligemma,mahadeva,bhairava,mahakal,kaali,shivaraj

# rg="poojya raghavendra namha"
# print(rg.capitalize())

# basav="basavanna"
# print(basav.capitalize())

# huli="huligemma"
# print(huli.capitalize())

# mh="mahadeva"
# print(mh.capitalize())

# bh="bhairava"
# print(bh.capitalize())

# mk="mahakal"
# print(mk.capitalize())

# lk="kaali"
# print(lk.capitalize())

# sh="shivarajdm"
# print(sh.capitalize())

#////////////////////////////////////////////////////////////////////////////////////

#center() center as per the given parameters and also padding also done

# rg="raghavendra namah"
# print(rg.center(50))    #while giving parameter no "" coma NO NO NO"""""""""""""


# bs="namo namo basavanna doore"
# print(bs.center(30,"!"))   #padding 

# bv="basavanna dore"
# print(bv.center(50))

# hl="huligemma udho udho"
# print(hl.center(50,"!"))

# hg="huligemma "
# print(hg.center(50))


# md="mahadevaya namaha"
# print(md.center(50,"$"))

# mv="mahadeva"
# print(mv.center(30))


# by="bhairava namah"
# print(by.center(80))

# bv="bhairava namaha"
# print(bv.center(30,"@"))

# mk="mahakal"
# print(mk.center(50))

# ml="mahakal namah"
# print(ml.center(50,"."))


# kal="kaali"
# print(kal.center(50))

# lm="kaali namaho namah"
# print(lm.center(50,"!"))

# sh="shivarajdmpowerful"
# print(sh.center(50,"!"))

# sd="shivraj"
# print(sd.center(50,"$"))

#/////////////////////////////////////////////////////////////////////////////////////////////

#count()  it will count the gives value occured in given string 

#raghavendra,basavanna,huligemma,mahadeva,mahakal,bhairava,kaali,shivaraj


# rh="raghavendraya namaha"
# print(rh.count("a"))    # we shoud give it in double/single inverted comma

# bs="basavanna namo namah"
# print(bs.count("n"))

# hl="huligemma namo namah"
# print(hl.count("m"))

# md="shambho mahadeva"
# print(md.count("h"))

# mk="mahakal devo devo namah"
# print(mk.count("k"))

# bh="aum bhairavaya namah"
# print(bh.count("r"))

# kl="kaali namo namo namo"
# countstr=kl.count("m")
# print(countstr)

# sh="shivaraj devendrappa makarabbi"
# countstr=sh.count("r")
# print(countstr)


#/////////////////////////////////////////////////////////////////////////////////

#endswith() OUTPUT=TRUE/FALSE
#raghavendra,basavanna,huligemma,mahadeva,mahakal,bhairva ,kali,shivraj

# rg="raghavendra namo namo!!!"
# print(rg.endswith("!"))

# rg="Raghavendra namo namo!!!"
# print(rg.endswith("namo",12))

# rg="Raghavendra namo namo!!!"
# print(rg.endswith("namo",12,16))

# bs="basavanna namo namo"
# print(bs.endswith("namo",10,14)) 

# hl="huligemma uddho uddho"
# print(hl.endswith("uddho",10,15))

# mh="Aum Mahadevaya Namah Namah"
# print(mh.endswith("Namah!"))

# mk="Mahakal shambho shiva"
# print(mk.endswith("shiva",16,22))

# bh="Aum Bhairavay Namah shambho"
# print(bh.endswith("shambho"))

# ka="kalike namo namah bhairavakalike namo"
# print(ka.endswith("namo"))

# sd="shivaraj very powerful person"
# print(sd.endswith("very"))

#////////////////////////////////////////////////////////////////////////////

#find() method 
        # it searches for first occurence of the given value and 
        # return the INDEX where it iz present ,(NUMERICAL VALUE)
        # if absent returns -1
#raghavendra,basavanna,huligemma,mahadeva,shiva,bhairava,mahakali

# rg="Aum shree raghavendraya namah"
# print(rg.find("shree"))

# bs="Aum Shiva basava"
# print(bs.find("basava"))

# huli="huligemma udho udho"
# print(huli.find("udho"))

# mh="mahadeva kashi namah"
# print(mh.find("kashi"))

# sh="shiva shiva hara hara"
# print(sh.find("shambho"))

# bh="bhairavaya namah namo"
# print(bh.find("namo"))

# mk="mahakal namo namah namo shiva"
# print(mk.find("namo"))

#///////////////////////////////////////////////////////////////////////////////////////

#index() method it gives index value of given word
#raghavendra,siddhoora,basavanna,huligemma,shiva,mahadeva,mahakal,bhairava,kaali


# rag="Raghavendraya namho namo namah"
# print(rag.index("namo"))

# sid="Aum shree guru siddharooda maharaj ki jai"
# print(sid.index("guru"))

# basav="Kuruvatti Basaveshwara Prasanna"
# print(basav.index("Prasanna"))

# hl="huligemma devi udho udho"
# print(hl.index("udho"))

# sh="shivaya namah shiva"
# print(sh.index("namah"))

# mh="mahadevaya shambho kailasa"
# print(mh.index("shambho"))

# mk="mahakaleshwra ujjaini"
# print(mk.index("ujjaini"))

# bhr="bhairava shiva shivaya"
# print(bhr.index("shiva"))

# kl="kaalike namostute"
# print(kl.index("kaalike"))

#/////////////////////////////////////////////////////////////////////////////////

#isalnum() return true if string consists of a-zA-Z 0-9 
#if any punctuation =false
#even no space shoud present
#raghavendra,siddhrooda,basavanna,huligemma,mahadeva,bhairava,kaali


# rg="raghavendrayanamah112"
# print(rg.isalnum())

# sid="siddharooda namo namah"
# print(sid.isalnum())

# basav="basavanna112"
# print(basav.isalnum())

# huli="huligemmadevi9"
# print(huli.isalnum())

# mh="mahadevaya namah"
# print(mh.isalnum())

# bh="bhairavayanamha112"
# print(bh.isalnum())

# kl="bhairavakalikenamostute"
# print(kl.isalnum())

#///////////////////////////////////////////////////////////////////////////////////

#isalpha() method return true only if a-zA=Z
#false=0-9,space,punctuation
#raghavendra.siddharooda,basavanna,huligemma,shiva,mahakal,bhairava,kaali

# rag="raghavendra"
# print(rag.isalpha())

# sidda="siddharooda112"
# print(sidda.isalpha())

# basav="basavanna"
# print(basav.isalpha())

# huli="huligemma23"
# print(huli.isalpha())

# sh="shiva"
# print(sh.isalpha())

# mh="mahakal112"
# print(mh.isalpha())

# bh="bhairava"
# print(bh.isalpha())

# kl="kaali8"
# print(kl.isalpha())

#/////////////////////////////////////////////////////////////////

#islower() returns true if all string in lowercase
#siddharooda raghavendra basavanna huligemma shiva bhairava mahakal kaali

# sd="siddharooda"
# print(sd.islower())

# rg="Raghavendra"
# print(rg.islower())

# bs="basavanna"
# print(bs.islower())

# huli="Huligemma"
# print(huli.islower())

# sh="shiva"
# print(sh.islower())

# mh="mahakaL"
# print(mh.islower())

# bh="bhairava"
# print(bh.islower())

# kl="kaali"
# print(kl.islower())

#///////////////////////////////////////////////////////////////////////

#isprintable() return true if all the given string is printable 
#"Hello!\nAre you #1?"----> false
# siddharooda raghavendra basavanna huligemma shiva bhairava kaali mahakal

# sd="siddharooda"
# print(sd.isprintable())

# rg="raghavendra"
# print(rg.isprintable())

# bs="basavan\nna"
# print(bs.isprintable())

# hl="huligemma\n"
# print(hl.isprintable())

# sh="shiva"
# print(sh.isprintable())

# mh="mahakal\n"
# print(mh.isprintable())

# bh="bhairava"
# print(bh.isprintable())

# kl="kaali"
# print(kl.isprintable)

#/////////////////////////////////////////////////////////////////////////////////////


#isspace() it returns only when a string contain white space else return false:
#siddarooa,raghavendra,basavanna,huligemma,mahakal,shiva,bhairava,kaali
# WHEN THERE IS ONLY A SPACE THEN ONLY IT IZ TRUE

# sd=" "
# print(sd.isspace())

# rg="    "
# print(rg.isspace())

# bs="    basavanna"
# print(bs.isspace())

# huli="huligemma         "
# print(huli.isspace())

# mh="mahakal  kaali"
# print(mh.isspace())

#////////////////////////////////////////////////////////////////////////////////////

#istitle() returns true only first letter of each word of  string is capitalized 
#siddharooda,raghavendra,huligemma,basavanna,shiva,mahakal,bhairav,kaali

# sd="Siddarooda Maharaj Ki Jai"
# print(sd.istitle())

# rg="raghavendraya Namah"
# print(rg.istitle())


# huli="HUligemma Udhho Udhoo"
# print(huli.istitle())

# basav="Basavanna Namo Namo"
# print(basav.istitle())

# sh="SHIVAYA NAMAH"
# print(sh.istitle())

# mh="Mahakal Namo Namo"
# print(mh.istitle())

# bh="Aum Bhairavaya Namah"
# print(bh.istitle())

#//////////////////////////////////////////////////////////////////////////////////////
# isupper() returns true only when all the characters of string is capital or upper case
#siddharooda raghavendra basavanna huligemma shiva mahakal bhairav kaali

# sd="SIDDAROODA MAHARAJ KI JAI"
# print(sd.isupper())

# rg="Raghavendra"
# print(rg.isupper())

# bs="BASAVANNA KI JAI"
# print(bs.isupper())

#/////////////////////////////////////////////////////////////////////

# startswith()  returns true if string is starts with a given word
#siddharooda raghavendra basavanna huligemma shiva bhairava mahakal kaali


# sd="sidda arooda shivaya namah"
# print(sd.startswith("sidda"))

# rg="Shree Raghavendraya Namah "
# print(rg.startswith("Shree"))

# bs="basavanna shivaya namah"
# print(bs.startswith("bas"))

# huli="Huligemma Devi Krupe"
# print(huli.startswith("huli"))   # should write as it izz

# sh="shivaya namah"
# print(sh.startswith("namah"))

#////////////////////////////////////////////////////////////////////////////////////////////


# swapcase()
       # ----> it will change case of character i.e UPPER TO lower && lower to UPPER


# sd="siddarooda"
# print(sd.swapcase())

# rg="RAGHAVENDRA"
# print(rg.swapcase())

# bs="baSAvaNNa"
# print(bs.swapcase())


# //////////////////////////////////////////////////////////////////////////////////////

# title()  it capitalizes each letter of the string
#raghavendra siddarooda basavanna huligemma shiva kali


rg="raghavendra namo namo"
print(rg.title())

sd="siddarooda NAmah NAmAH"
print(sd.title())

#////////////////////////////////////////////////////////////////////////////////////////