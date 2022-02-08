#Python Basic Grade Category per Average

print ("\nGRADES AVERAGE PROGRAM")

math = float(input("Math grade: "))
english = float(input("English grade: "))
science = float(input("Science grade: "))
pe = float(input("P.E. grade: "))
history = float(input("History grade: "))

grade = [math,english,science,pe,history]

if math < 75 or english < 75 or science < 75 or pe < 75 or history < 75:

    print ("Please pass your failed subject/s!")

average = sum(grade)/5

print ("Your Average is " + str(average))

if average > 100 or average <= 50:
    print("Invalid Grade")
elif average >= 98:
        print("With Highest Honor")
elif average >= 95:
     print("With High Honor")
elif average >= 90:
        print("With Honor")
elif average >= 75:
        print("Passed")
else:
        print("Failed")

print ("\n")