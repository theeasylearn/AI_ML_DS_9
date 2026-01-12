tup=(1,2,3,4,5,3)
tuple1=( 'Ankit', 456 , 1.14, 'Patel', 70.2,True,False)

# Print complete tuple
print(tup)

# Print first element of the tuple
print(tuple1[0])

# Print elements starting from 2nd till 3rd
print(tuple1[1:3])

# Print elements starting from 3rd element
print(tuple1[3:])

# Print tuple two times
print(tup*2)

# Print concatenated tuple
print(tup+tuple1)

#count
print(tup.count(3))

#index
print(tuple1.index('Patel'))