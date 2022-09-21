# 1)Even and Odd
num = int(input("Enter the number: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

############################################################

# 2)Prime number
num = int(input("Enter the number: "))
if num>1:
    for i in range(2,num):
        if (num%i) == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime") 
else:
   print(f"{num} is not prime")

##############################################################

# 3)Leap Year
year = int(input("Enter the year: "))
if ((year%4==0) and (year%100!=0)) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

##############################################################

# 4)Swapping
input1 = input("Enter your 1st value: ")
input2 = input("Enter your 2nd value: ")

print(f"input1 is {input1} , input2 is {input2}")

input1,input2=input2,input1

print(f"after swapping, input1 is {input1}")
print(f"after swapping, input2 is {input2}")

###############################################################

# 5)Palindrom String
str = input("Enter your word: ")
reverse_str = str[::-1]
if str==reverse_str:
    print(f"{str} is palindrom")
else:
    print(f"{str} is not palindrom")

###############################################################

# 6) Palindrom number
num = int(input("Enter your number: "))
temp=num
rev_num = 0
while num>0:
    remainder = num%10 
    rev_num = (rev_num * 10) + remainder
    num = num // 10
if temp==rev_num:
    print(f"{temp} is a palindrom")
else:
    print(f"{temp} is not a palindrom")

###############################################################

# 7)Sum of digit
num = input("Enter your number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(f"Sum of digits of the given number is {sum}")

###############################################################

# 8)Reversing the String
str = input("enter your string: ")
rev_str = str[::-1]
print(f"the reversed string for {str} is {rev_str}")

###############################################################

# 9)Reversing the Number
# method1
num_str = input("Enter the number: ")
rev_num_str = num_str[::-1]
num_int = int(rev_num_str)
print(f"reversed number is {num_int}")

# method2
num = int(input("Enter your number: "))
temp = num
rev_num = 0
while num>0:
    remainder = num%10 #it will store the last digit of the given number
    rev_num = (rev_num * 10) + remainder
    num = num // 10 # returns  quotient value
print(f"Reversed number of {temp} is {rev_num}")
'''
for example
num = 123                 num = 12                 num = 1
remainder = 123%10        remainder = 12%10        remainder = 1%10
          = 3                       = 2                      = 1
rev_num = 0*10+3          rev_num = 3*10+2         rev_num = 32*10+1
    = 3                       =32                      = 321
num = 123//10             num = 12//10             num = 1//10
    = 12                      = 1                      = 0
'''

###############################################################

# 10)Perfect Number
"A perfect number is a positive integer that is equal to the sum of it's proper divisors"
num = int(input("Enter your number: "))
sum = 0
for i in range(1,num):
    if (num%i==0):
        sum = sum + i
if (sum==num):
    print("perfect")
else:
    print("not perfect")

###############################################################

# 11)Fibonacci Series
'A series of numbers in which each number is sum of two preeceding numbers'
num = int(input("Enter any number: "))
n1 = 0
n2 = 1
sum = 0
if num <= 0:
    print("invalid input")
else:
    for i in range(num):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1+n2
