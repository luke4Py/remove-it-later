gender = input("Enter your gender: ")
age = int(input("Enter your age: "))
if gender == "male":
    if age>=1 and age<=10:
        print("Section1")
    elif age>=11 and age<=20:
        print("Section2")
    elif age>=20:
        print("Section3")
elif gender == "female":
    if age>=1 and age<=10:
        print("Section1")
    elif age>=11 and age<=20:
        print("Section2")
    elif age>=20:
        print("Section3")

