fruit = ['Apple', 'Banana', 'Orange']

print(fruit[0])
print(fruit[-1])

fruit[1] = 'Pear'
print(fruit)

fruit.append('Pineapple')
print(fruit)

fruit.insert(1, 'Mango')
print(fruit)

del fruit[0]
print(fruit)

fruit.pop()
print(fruit)

myfruit = fruit.pop(1)
print(myfruit)
print(fruit)

fruit.remove('Mango')
print(fruit)

