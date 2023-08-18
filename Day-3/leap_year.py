"""A program that checks if an year is leap

It returns Leap if the year is leap, else it returns Not Leap"""

year = int(input("Enter an year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap")
        else:
            print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")