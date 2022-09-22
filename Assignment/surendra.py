gender =str(input("Enter your gender : "))
age= int(input("Enter your age : "))
gender= gender.lower()
if gender == "male":
    if age>=1 and age<=10:
        print ("section 1")
    elif age>=11 and age<=20:
        print ("section 2")
    elif age>=20:
        print ("section 3")
elif gender == 'female':
    if age>=1 and age<=10:
        print ("section 4")
    elif age>=11 and age<=20:
        print ("section 5")
    elif age>=20:
        print ("section 6")