#assignment 1
'''
Write code in your laptop and share the same to me personally.

input : "You ARe in PythoN21 BtacH"
output : Your code should provide output as -> "yOU arE IN pYTHOn21 bATCh"

Submission Date : Today(i.e 19-09-22) End of day.'''

from re import A


input = "You ARe in PythoN21 BtacH"
output = print( "You ARe in PythoN21 BtacH".swapcase())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#assignment 2

#set

brands = {"maruti","ford","toyota","hyundai","fiat","bmw","volksvwagon","mercedes"}
brands.add("jaguar")
brands

a = brands.copy()

a.clear()
a

brands
brands.discard("maruti")
brands.pop()
print brands

brands.remove("bmw")
brands.add("mercedes")
brands.add("bmw")



#shows differences
a = {1,2,3,4}
b = {2,3,4,5}
c = a.difference(b)
c
#updates differences
x = {"apple", "banana", "mango"}
y = {"mango", "cherry", "apple"}

x.difference_update(y)

print(x)

#Return a set that contains all items from both sets, except items that are present in both sets:
x = {"21", "31", "41", "71", "61"}
y = {"51", "61", "71"}

z = x.symmetric_difference(y)

print(z)

#Return a set that contains all items from both sets, duplicates are excluded:
x = {1,2,3,4}
y = {5,6,2,1}

z = x.union(y)

print(z)

#shows the similar ones
a = {1,2,3,4}
b = {5,6,2,1}
c = a.intersection(b)
c
#shows the updated similar ones
a = {1,2,3,4}
b = {5,6,2,1}
c = a.intersection_update(b)
a #similar values are updated and non similar values are removed


#is true or not
x = {"Ca", "Mg", "Fe"}
y = {"Ce", "Al", "Mn"}

z = x.isdisjoint(y)

print(z)

#Return True if all items in set x are present in set y
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

# Insert the items from set y into set x:
x = {"a", "b", "c"}
y = {"d","e","f"}

x.update(y)
print(x)



