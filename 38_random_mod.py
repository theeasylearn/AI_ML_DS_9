import random

print(random.random())
print(random.uniform(50,100))
print(random.randint(50,100))
print(random.randrange(0,100,10))

colors=['red','white','blue','green']
print(random.choice(colors))
print(random.choices(colors,k=2))
random.shuffle(colors)
print(colors)
print (random.sample(colors, 4))
print(colors)

name='Diksha Patel'
print(name.upper())
print(name.lower())