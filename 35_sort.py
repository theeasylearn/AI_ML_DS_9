#sorted(iterable, key=None, reverse=False)

lit=[10,3,56,34,9,0]

print(sorted(lit))
print(sorted(lit,reverse=True))

dict={
    'jan':2,
    'fab':67,
    'mar':34,
    'apr':7
}

print(sorted(dict))
print(list(sorted(dict,key=lambda x:x[2])))