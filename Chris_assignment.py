#assignment
'''Assignment Task 01_120922

take two inputs and store them in gender and age variables, 
later print the appropriate section based on their age and gender
(refer below string for print statements for gender and ages)

"""
section1(M1-10)
section2(M11-20)
section3(M20-above)

section4(F1-10)
section5(F11-20)
section6(F20-above)
"""


Example : 
input : 
-> Gender = 'Male'
-> Age	= 14

output:
Section2

explanation:
As given above in the reference part, the inputs lie between M11-M20 
which corresponds to the output section2. Hence section2 is printed.
'''
#range function used 
Input_age = int(input())
Input_gender = input("Enter your gender")

if Input_gender == "male":
   if Input_age in range(1, 10):
      print("Belongs to group 1")
   elif Input_age in range(11, 20):
        print("Belongs to group 2")
        
   else:
      print("Belongs to group 3")
if Input_gender == "female":
   if Input_age in range(1, 10):
        print("Belongs to group 4")
   elif Input_age in range(11, 20):
        print("Belongs to group 5")
   else: 
    print("Belongs to group 6")


