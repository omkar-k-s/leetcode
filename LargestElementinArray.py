arr = [10, 45, 67, 89, 32]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)