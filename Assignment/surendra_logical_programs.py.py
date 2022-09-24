#1) Even or Odd
num = int(input("Enter any number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#2) Prime number or not
num = int(input("Enter any number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

#3) Leap year or not
year = int(input("enter any year: "))
if year%400==0 or year%4==0 and year%100==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#4) Swapping
#swapping a string from lowercase to uppercase or uppercase to lowercase
text = str(input("enter any text: "))
print(text.swapcase())

#swapping of values from one variable to another
var1 = input("enter any value: ")
var2 = input("enter any value: ")
print(f" before swapping var1 is {var1} and var2 is {var2}")
var1,var2=var2,var1
print(f"after swapping var1 is {var1} and var2 is {var2}")

#5) Fibonacci series
num = int(input("enter any number: "))
n1 = 0
n2 = 1
sum = 0
if num>0:
    for i in range(num):
        print(sum)
        n1=n2
        n2=sum
        sum=n1+n2
else:
    print("invalid number")

#6) Palindrome number
num = int(input("enter any number: "))
rev = int(str(num)[::-1])
if num == rev:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

#7) Reversing the number
num = int(input("enter any number: "))
rev = int(str(num)[::-1])
num_rev=rev
print(f"The reverse of {num} is {num_rev} ")

#8) Sum of digits
num = input("enter any number: ")
sum = (0)
for i in num:
    sum = sum + int(i)
print(f"The sum of the digits for {num} is {sum}")

#9) Perfect number
num = int(input("enter any number: "))
for i in range(num):
    if i*i==num:
        print(f"{num} is a perfect square.")
        break
else:
    print(f"{num} is not a perfect square.")

#10) Palindrome string
text = input("enter any text: ")
rev = text[::-1]
if text==rev:
    print(f"{text} is a palindrome string")
else:
    print(f"{text} is not a palindrome string")

#11) Reversing the string
text = input("enter any text: ")
rev = text[::-1]
text_rev=rev
print(f"The reverse of {text} is {text_rev}")
