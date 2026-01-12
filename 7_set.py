#creating a set 

fruits={'Apple','Banana','Grapes','Papaya'}
print(fruits)

#Adding elements to a set
fruits.add('Mango')
print(fruits)

#Removing element from a set
fruits.remove('Apple')
print(fruits)

#set operations
set1={1,2,3}
set2={2,3,4}

union=set1.union(set2)
print(union)
intersection=set1.intersection(set2)
print(intersection)
difference=set2.difference(set1)
print(difference)


#multiline statement
item_one=1
item_two=2
item_three=3
Total = item_one + \
item_two + \
item_three