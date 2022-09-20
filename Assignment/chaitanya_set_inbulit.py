##add()
##add()	Adds an element to the set
##If the element already exists, the add() method does not add the element.

Names = {"chaitanya", "Ahmad", "Ali"}
Names.add("Luke")
print(Names)

##clear()
##	Removes all the elements from the 

Names = {"chaitanya", "Ahmad", "Ali"}
Names.clear()
print(Names)

##copy()	
# Returns a copy of the set
##The copy() method copies the set.

Names = {"chaitanya", "Ahmad", "Ali"}
Names.copy()
print(Names)

##difference()
##Returns a set containing the difference between two or more 
##Meaning: The returned set contains items that exist only in the first set, and not in both sets.

x = {"chaitanya", "Ahmad", "Ali"}
y = {"gpay", "paytm", "phonepey"}

z = x.difference(y)

print(z)

##Reverse the first example. Return a set that contains the items that only exist in set y, and not in set x:

x = {"chaitanya", "Ahmad", "Ali"}
y = {"gpay", "paytm", "phonepey"}

z = y.difference(x)

print(z)


##difference_update()

##Removes the items in this set that are also included in another, specified set
##The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

x = {"chaitanya", "Ahmad", "Ali"}
y = {"gpay", "paytm", "phonepey"}
x.difference_update(y)
print(x)

##discard()

##Remove the specified item
##This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not
Names = {"chaitanya", "ahmad", "ali"}

Names.discard("ahamd")

print(Names)

##intersection()

##Returns a set, that is the intersection of two other sets
##Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
z = x.intersection(y)
print(z)
##Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

##intersection_update()

##Removes the items in this set that are not present in other, specified set(s)
##The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
x.intersection_update(y)
print(x)
##Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

##isdisjoint()

##Returns whether two sets have a intersection or not
##The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
x.intersection_update(y)
print(x)
##What if no items are present in both sets?
##Return False if one ore more items are present in both sets:
x = {"chaitanya", "ahmad", "ali"}
y = {"gpay", "paytm", "phonepey"}
z = x.isdisjoint(y)
print(z)

##issubset()

##Returns whether another set contains this set or not
##The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
##What if not all items are present in the specified set?
##Return False if not all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

##issuperset()

##Returns whether this set contains another set or not
##The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
##What if not all items are present in the specified set?
##Return False if not all items in set y are present in set x:

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

##pop()	

##Removes an element from the set
Names = {"chaitanya", "ahmad", "ali"}
Names.pop()
print(Names)
##Return the removed element
Names = {"chaitanya", "ahmad", "ali"}
x = Names.pop()
print(x)


##remove()	

##Removes the specified element
##This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not
Names = {"chaitanya", "ahmad", "ali"}
Names.remove("banana")
print(Names)

##symmetric_difference()

##Returns a set with the symmetric differences of two sets
##The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
z = x.symmetric_difference(y)
print(z)

##symmetric_difference_update()

##inserts the symmetric differences from this set and another
##The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.

x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
x.symmetric_difference_update(y)
print(x)


##union()
	
##Return a set containing the union of sets
##You can specify as many sets you want, separated by commas.
##It does not have to be a set, it can be any iterable object.
##If an item is present in more than one set, the result will contain only one appearance of this item.
x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
z = x.union(y)
print(z)
##Unify more than 2 sets:
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)


##set update()

##The update() method updates the current set, by adding items from another set (or any other iterable).
##If an item is present in both sets, only one appearance of this item will be present in the updated set.

##Insert the items from set y into set x:
x = {"Chaitanya", "ahmad", "ali"}
y = {"google", "paytm", "phonepay"}
x.update(y)
print(x)