lst = []
num = int(input('enter the numbers: '))

for n in range(num):
    numbers = int(input(' '))
    lst.append(numbers)
    
print("Sum of elements in given list is :", sum(lst))