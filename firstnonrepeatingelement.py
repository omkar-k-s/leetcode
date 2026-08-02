arr = [2, 3, 4, 2, 3, 5, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break