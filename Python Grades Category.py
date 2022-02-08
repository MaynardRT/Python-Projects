#Python Basic Grade Category per Average

print ("\nGRADES AVERAGE PROGRAM")

math = float(input("\nMath grade: "))
english = float(input("\nEnglish grade: "))
science = float(input("\nScience grade: "))
pe = float(input("\nP.E. grade: "))
history = float(input("\nHistory grade: "))

grade = [math,english,science,pe,history]

if math < 75 or english < 75 or science < 75 or pe < 75 or history < 75:

    print ("Please pass your failed subject/s!")

average = sum(grade)/5

print ("Your Average is " + str(average))

if average > 100 or average <= 50:
    print("\nInvalid Grade")
elif average >= 98:
        print("\nWith Highest Honor")
elif average >= 95:
     print("\nWith High Honor")
elif average >= 90:
        print("\nWith Honor")
elif average >= 75:
        print("\nPassed")
else:
        print("\nFailed")

print ("\n")
