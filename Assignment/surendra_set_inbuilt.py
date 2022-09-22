##set inbuilt methods##

#1) add()
# This method is used to add an element to a set and the element will be added anywhere as a set is orderless.
#example:
set1 = {"a", "b", "c"}
set1.add("d")
print(set1)
# This method does not allow duplicate values
#example:
set2 = {"x", "y", "z"}
set2.add('y')
print(set2)

#2) clear()
# This method is used to remove all the elements from the set
#example:
set1 = {"a", "b", "c"}
set1.clear()
print(set1)

#3) copy()
# This method is used to return a copy of a set
#example:
set1 = {"a", "b", "c"}
set1.copy()
print(set1)

#4) difference()
# This method is used to return a set of difference between sets i.e the common elements will be removed and remaining elements in the first set will be displayed in a new set.
#example:
set1 = {"a", "b", "c"}
set2 = {"a", "e", "c"}
set3 = set1.difference(set2)
print(set3)

#5) difference_update()
# This method is used to remove common elements from the sets and return the first set.
#example:
set1 = {"a", "b", "c"}
set2 = {"a", "e", "c"}
set1.difference_update(set2)
print(set1)

#6) discard()
# This method is used to remove a specified element from the set.
#example:
set1 = {"a", "b", "c"}
set1.discard("b")
print(set1)

#7) intersection()
# This method is used to return a set, that is intersection of given sets i.e only the common elements in the sets will be displayed in a new set.
#example:
set1 = {"a", "b", "c"}
set2 = {"a", "e", "f"}
set3 = set1.intersection(set2)
print(set3)

#8) intersection_update()
# This method is similar to intersection() method but the elements will be displayed in first set not in a new set.
#example:
set1 = {"a", "b", "c"}
set2 = {"a", "e", "c"}
set1.intersection_update(set2)
print(set1)

#9) isdisjoint()
# This method is used to know whether the set have an intersection or not i.e it returns true if no common elements is present in sets else it returns false.
#example:
set1 = {"a", "b", "c"}
set2 = {"z", "e", "f"}
print(set1.isdisjoint(set2))

#10) issubset()
# This method is used to know whether all the elements in a set are present in another set.
#example:
set1 = {"a", "b", "c"}
set2 = {"a", "q", "b", "c", "z"}
set3 = set1.issubset(set2)
print(set3)

#11) issuperset()
# This method is used to know whether a set contains another set also.
#example:
set1 = {"a", "b", "c", "x", "y", "z"}
set2 = {"x", "b", "z"}
set3 = set1.issuperset(set2)
print(set3)

#12) pop()
# This method will remove an element from the list and returns its value.
#example:
set1 = {"a", "b", "c"}
set1.pop()
print(set1)

#13) remove()
# This method is used to remove specific element from the set and will raise an error if the element is not present in the set.
#example:
set1 = {"a", "b", "c"}
set1.remove("c")
print(set1)
# If the element is not present in the list it will raise an error.
#example:
set1 = {"a", "b", "c"}
set1.discard("z")
print(set1)

#14) symmetric_difference()
# This method returns a set with the common elements in both sets and elements in main or first set.
#example:
set1 = {"a", "b", "c"}
set2 = {"x", "b", "c"}
set1.symmetric_difference(set2)
print(set1)

#15) symmetric_difference_update()
# This method returns a set with elements that are not common in both sets.
#example:
set1 = {"a", "b", "c"}
set2 = {"x", "b", "c"}
set1.symmetric_difference_update(set2)
print(set1)

#16) union()
# This method is used to combine all the elements in both sets.
#example:
set1 = {"a", "b", "c"}
set2 = {"x", "b", "c"}
set3 = set1.union(set2)
print(set3)

#17) update()
# This method is used to update or add elements from another set. This method is similar to union() method but we do not need a new set for output here.
#example:
set1 = {"a", "b", "c", "d"}
set2 = {"x", "b", "c"}
set1.update(set2)
print(set1)











