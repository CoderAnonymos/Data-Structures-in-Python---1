fruits = ["Apple", "Banana", "Grape", "Mango", "Blueberry", "Strawberry", "Blackberry", "Papaya", "Guava"]

print("Lemgth of the list is: ", len(fruits))
print("First Element of the list is: ", fruits[0])
print("Last Element of the list is: ", fruits[-1])

fruits.append("Watermelon")

print("Updated List: ", fruits)

fruits.remove("Guava")

print("Updated List: ", fruits)

fruits.sort()

print("Updated List: ", fruits)

fruits.pop(2)

print("Updated List: ", fruits)

fruits.reverse()

print("Reversed List: ", fruits)
print("Doubled List: ", fruits * 2)

fruits = fruits[:4]

print("Sliced List: ", fruits)

fruits.clear()

print("Cleared List: ", fruits)