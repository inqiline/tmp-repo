numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
number = numbers.index(None)

total = 0
count = 0
for num in numbers:
    if num is not None:
        total += num
        count += 1
average = total / len(numbers)
numbers[number] = average

print("Измененный список:", numbers)

