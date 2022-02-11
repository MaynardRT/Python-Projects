#Basic Age and Height Differenciator


print ("\nAge and Height Notification")
print ("\n")
age = int(input("\nPlease enter your age: "))
height = int(input("\nPlease enter your height in CM: "))

if age >= 18 and height >= 176:
    print ("\nTall and Legal Age")
elif age >= 18 and height >= 150:
    print ("\nAverage and Legal Age")
elif age >= 18 and height >= 100:
    print ("\nSmall and Legal Age")
elif age < 18 and height <= 150:
    print ("\nShort and Underage")
else:
    print("\nUnderage")
    
print ("\n")
