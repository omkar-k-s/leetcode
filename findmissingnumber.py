arr = [1,2,4,5,6]

n = len(arr) + 1

expected = n * (n + 1) // 2

actual = sum(arr)

print(expected - actual)