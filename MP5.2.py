numbers = [18, 19, 20]

#Name : Ivan Banaag
#School : FEU TECH
#MACHINE PROBLEM NUMBER : 3

numbers[1] = 17

print ("Name : Ivan Banaag")
print ("School : FEU TECH")
print ("MACHINE PROBLEM NUMBER : 3")

print ("a", numbers)

numbers.append(4)
numbers.append(5)
numbers.append(6)

print("b", numbers)

numbers.pop(0)
print ("c", numbers)

numbers.sort()
print ("d", numbers)

num = numbers + numbers

print ("e", num)

num.insert(3, 25)
print ("f", num)