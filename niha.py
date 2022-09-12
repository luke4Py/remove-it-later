gender = input("Enter your gender: ") 
age =  int(input("Enter your age: "))
if gender == "male":
 if age>=1 and age<=10:
  print("Section 1")
 elif age>=11 and age<=20:
  print("Section 2")
 else:
  print("Section 3")
elif gender == "female":
 if age>=1 and age<=10:
  print("Section 4")
 elif age>=11 and age<=20:
  print("Section 5")
 else:
  print("Section 6")
