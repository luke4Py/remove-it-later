'''
1)add()
   a)adds an element to the set

   b)we can not add exixting element to the set
'''
#example
name = {'satabdi','ria','rohan'}
name.add('arun')
print(name)

'''
2)clear()
  a)removes all the elements from the set
'''
#example
name = {'satabdi','ria','rohan'}
name.clear()
print(name)

'''
3)copy()
  a)returns a copy of the set
'''
#example
name = {'satabdi','ria','rohan'}
name.copy()
print(name)

'''
4)difference()
  a)returns a set containing the difference between two or more sets

  b)the returned set contains items that exist only in the first set, and not in both sets
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'ria','arun','arnab'}
name3 = name1.difference(name2)
print(name3)

'''
5)difference_update()
  a)removes the items in this set that are also included in another specified set

  b)the difference_update() method is different from the different() method, 
  because the difference() method returns a new set, without the unwanted items, 
  and the difference_update() method removes the unwanted items from the original set
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'ria','arun','arnab'}
name1.difference_update(name2)
print(name1)

'''
6)remove()
  a)remove the specified element
'''
#example
name1 = {'satabdi','ria','rohan'}
name1.remove('ria')
print(name1)

'''
7)discard()
  a)remove the specified item

  b)this method is different from the remove() method, because the remove() method
  will raise an error if the specified item does not exist, and the discard() method
  will not.
'''
#example
name1 = {'satabdi','ria','rohan'}
name1.discard('satabdi')
print(name1)

'''
8)intersection()
  a)returns a set, that is the intersection of two or more sets

  b)the returned set contains only items that exist in both sets, or in all sets if the
  comparison is done with more than two sets
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'rohan','arun','ratna'}
name3 = name1.intersection(name2)
print(name3)

'''
9)intersection_update()
  a)removes the item in the set that are not present in other specified set(s)

  b)the intersection_update() method is diffrent from the intersection() method,
  because the intersectin() method returns a new set without the unwanted, and the
  intersection_update() method removes the unwanted items from the original set
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'rohan','arun','ratna'}
name3 = {'rohan','arnab','gracy'}
name1.intersection_update(name2,name3)
print(name1)

'''
10)isdisjoint()
  a)returns whether two sets have a intersection or not

  b)The isdisjoint() method returns True if none of the 
  items are present in both sets, otherwise it returns False.
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'ratna','arun','arnab'}
result = name1.isdisjoint(name2)
print(result)

'''
11)issubset()
  a)returns whether another set contains this set or not

  b)The issubset() method returns True if all items in the 
  set exists in the specified set, otherwise it retuns False.
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'ratna','arun','arnab','satabdi','ria','rohan'}
result = name1.issubset(name2)
print(result)

'''
12)issuperset()
  a)returns whether this set contains another set or not

  b)The issuperset() method returns True if all items in the 
  specified set exists in the original set, otherwise it retuns False.
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'ratna','arun','arnab','satabdi','ria','rohan'}
result = name2.issuperset(name1)
print(result)

'''
13)pop()
  a)removes an element from the set
'''
#example
name1 = {'satabdi','ria','rohan'}
name1.pop()
print(name1)

'''
14)symmetric_difference()
  a)returns a set with the symmetric difference of two sets i.e
  this mwthod returns a set that contains all items from both set,
  but not the items that are present in both sets.

  b)symmetric_difference() returns set contains a mix of items that are not
  present in both sets
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'rohan','arun','ratna'}
result = name1.symmetric_difference(name2)
print(result)

'''
15)symmetric_difference_update()
  a)this method updates the original set by removing items that are present in
  both sets, and inserting the other items
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'rohan','arun','ratna'}
name1.symmetric_difference_update(name2)
print(name1)

'''
16)union()
  a)the union() method returns a set that contains all items from the original set, 
  and all items from the specified set(s).

  b)you can specify as many sets you want, separated by commas.

  c)it does not have to be a set, it can be any iterable object.

  d)if an item is present in more than one set, the result will contain only one appearance of this item.
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'rohan','arun','ratna'}
name3 = {'rohan','arnab','gracy'}
name4 = ['gracy','mona','Ria'] #point(c)
result = name1.union(name2,name3,name4) #point (b)
print(result)

'''
17)update()
  a)the update() method updates the current set, by adding items from another set (or any other iterable).

  b)if an item is present in both sets, only one appearance of this item will be present in the updated set.
'''
#example
name1 = {'satabdi','ria','rohan'}
name2 = {'rohan','arun','ratna'}
name3 = {'rohan','arnab','gracy'}
name4 = ['gracy','mona','Ria']
name1.update(name2,name3,name4)
print(name1)