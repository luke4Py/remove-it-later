#even or odd

my_list = [1,2,3,4,5,6,7,8,9,10]
list(map(lambda x : x % 2 == 0, my_list))

#prime number

find_prime = int(float(input("enter value: ")))
result = all(list(map(lambda x: (x % 2), (range(2, find_prime)))))
print(result)

#leap year or not
#by creating my local function and calling it outside #using return:

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

leap_year(2000)

#swapping
a,b = "hello", "hi"
a,b = b,a
print (a,b)

#fibonacci series using lambda - reduce()
def fibonacci_series(count):
    fibonacci_series = [0,1]
    list(map(lambda x : fibonacci_series.append(sum(fibonacci_series[-2:])), range(2,count)))
    return fibonacci_series[:count]

fibonacci_series(15)
fibonacci_series(21)

#pallindrome_number
number=int(input("Enter a number:"))
temporary=number
reverse=0
while(number>0):
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
if(temporary==reverse):
    print("ITS A PALINDROME!")
else:
    print("ITS NOT A PALLINDROME!")

#reverse_number
number=int(input("Enter a number:"))
reversed_number=0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print("Reversed Number: " + str(reversed_number))

#sum of the digits:
def Sum_of_digit(x):
    
    sum = 0
    for digit in str(x): 
      sum = sum + int(digit)      
    return sum

#perfect_number
Perfect_number = int(input("Enter any number: "))
sum = 0
for i in range(1, Perfect_number):
    if(Perfect_number % i == 0):
        sum += i
if (sum == Perfect_number):
    print(f"{Perfect_number} ITS A PERFECT NUMBER")
else:
    print(f"{Perfect_number} ITS NOT A PERFECT NUMBER")

#find perfect number of given p
lambda p : 2**(p−1) * ((2**p) − 1)

Sum_of_digit(1234)

#pallindrome string
def pallindrome(my_string):
    if my_string == my_string[::-1]:
        print("IS A PALLINDROME")
    else:
        print("ITS NOT A PALLINDROME")

#reverse string
print(''.join(reversed(input())))




