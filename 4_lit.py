colors=['red','blue','green','pink','orange']
detail=["Drashti",13,4.50,True]
duplicate=[1,2,3,4,2,1,3]
# Print complete list
print(colors)

# Print first element of the list
print(colors[0])

# Print elements starting from 1st till 3rd
print(colors[0:3])

# Print elements starting from 2nd element
print(colors[2:])

# Print list two times
print(colors*2)

# Print concatenated lists
print(colors+detail)

colors.append("black")
print(colors)

colors.extend(['a','b'])
print(colors)

colors.insert(4,"white")
print(colors)

colors.remove("a")
print(colors)

print(colors.pop(7))
print(colors)

detail.clear()
print(detail)

print(duplicate.index(2))
print(duplicate.count(3))
duplicate.sort()
print(duplicate)

duplicate.reverse()
print(duplicate)

copy_lit=colors.copy()
print(copy_lit)