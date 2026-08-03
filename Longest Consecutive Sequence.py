def longest_consecutive(arr):

    num_set = set(arr)

    longest = 0

    for num in num_set:

        if num - 1 not in num_set:

            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100,4,200,1,3,2]

print(longest_consecutive(arr))