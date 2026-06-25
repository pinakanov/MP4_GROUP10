numbers = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39, 71, 55, 41, 95, 70, 48, 42, 32, 13, 35]

#Name : Ivan Banaag
#School : FEU TECH
#MACHINE PROBLEM NUMBER : 3

print ("Name : Ivan Banaag")
print ("School : FEU TECH")
print ("MACHINE PROBLEM NUMBER : 3")

print("a", numbers)

ave = sum(numbers) / len(numbers)
print("b average = ", ave)

largest = max(numbers)
smallest = min(numbers)
print("c largest = ", largest, "___", "smallest = ", smallest)

sorted_unique = sorted(set(numbers))
second_smallest = sorted_unique[1]
second_largest = sorted_unique[-2]
print("d second largest = ", second_largest, "second smallest = ", second_smallest)

even = 0
for n in numbers:
    if n % 2 == 0:
        even += 1

print("e even numbers = ", even)

odd = 0 
for nu in numbers:
    if nu % 2 != 0:
        odd += 1

print("f odd numbers = ", odd)




