arr = [ 10, 40, 50, 89, 60, 66]

largest = float("-inf")
second = float("-inf")

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest > num >second:
        second = num
print(second)
