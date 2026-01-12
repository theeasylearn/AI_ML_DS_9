dict={
    'name':'the easy learn',
    'age':20,
    'size':30.33,
    'available':True
}

#print whole dictionary
print(dict)

#print specific value from dictionary
print(dict['available'])

#change value of perticular key
dict['name']="mobile"
print(dict)

#delete specific key value pair
del dict['age']
print(dict)

#create an empty dictionary
emp_dict={}
print(emp_dict)

#adding elements one at a time
emp_dict['author']="mr. shreekant"
emp_dict['age']=50
print(emp_dict)

#adding set of values to a single key
emp_dict['books']=('energy','power','tree','sea','forest')
emp_dict['chapters']=[1,2,3,4,5,6]
print(emp_dict)

emp_dict.clear()
print(emp_dict)

print(emp_dict.copy())

print(dict.get('size',123))

print(dict.items())

print(dict.keys())

lit1=[1,2,3,4,5]
print(dict.fromkeys(lit1,[123]))

print(dict.pop('available','no item found'))
print(dict.pop('a','no item found'))

dict2={
    'num1':1,
    'num2':2,
    'num3':3,
    'num4':4
}
dict3={
    'name':'numbers',
    'num1':'1',
    'num3':6
}

dict2.update(dict3)
print(dict2)

print(dict3.values())