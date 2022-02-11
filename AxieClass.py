#Basic Axie Dictionary


print ("\nList of Axies")
print ("\n")

AxieClass = (
    "1.Bird", "2.Mech", "3.Plant", "4.Beast", "5.Reptile", "6.Aquatic", "7.Dusk", "8.Bug", "9.Dawn"
)

Bird = {

    "Strength" : 35,
    "Speed" : 61,
    "Health" : 301,
}

Mech = {

    "Strength" : 34,
    "Speed" : 55,
    "Health" : 320,
}

Plant = {

    "Strength" : 54,
    "Speed" : 34,
    "Health" : 540,
}

Beast = {

    "Strength" : 40,
    "Speed" : 45,
    "Health" : 314,
}

Reptile = {
    
    "Strength" : 38,
    "Speed" : 43,
    "Health" : 401,
}

Aquatic = {

    "Strength" : 43,
    "Speed" : 59,
    "Health" : 468,
}

Dusk = {

    "Strength" : 41,
    "Speed" : 49,
    "Health" : 449,
}

Bug = {

    "Strength" : 37,
    "Speed" : 55,
    "Health" : 347,
}

Dawn = {

    "Strength" : 45,
    "Speed" : 52,
    "Health" : 447
}


print (AxieClass)

axie = int(input("\nSelect Class from the List of Axies above: "))

if (axie == 1):
    print ("\nHere's the stats of" + " " + "Bird " + str(Bird))
elif (axie == 2):
    print ("\nHere's the stats of" + " " + "Mech " + str(Mech))
elif (axie == 3):
    print ("\nHere's the stats of" + " " + "Plant " + str(Plant))
elif (axie == 4):
    print ("\nHere's the stats of" + " " + "Beast " + str(Beast))
elif (axie == 5):
    print ("\nHere's the stats of" + " " + "Reptile " + str(Reptile))
elif (axie == 6):
    print ("\nHere's the stats of" + " " + "Aquatic " + str(Aquatic))
elif (axie == 7):
    print ("\nHere's the stats of" + " " + "Dusk " + str(Dusk))
elif (axie == 8):
    print ("\nHere's the stats of" + " " + "Dawn " + str(Dawn))
else:
    print ("\nInvalid! Exit... ")

print ("\n")