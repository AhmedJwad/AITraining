numbers=[5,10,15,20,25,30]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[:3])
print(numbers[-2:])
numbers.append(35)
print(numbers)
numbers.remove(15)
print(numbers)

for number in numbers:
 print(number)

 for index, number in enumerate(numbers):
   print(index , number)

numbers=[1,2,3,4,5,6,7,8,9,10]
squared=[n * n for n in numbers]

print(squared)

even=[n * n for n in numbers if n % 2==0]

print(even)

