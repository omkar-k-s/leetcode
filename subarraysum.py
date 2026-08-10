def subarray_sum(arr, k):

    prefix = {0: 1}

    current_sum = 0
    count = 0

    for num in arr:

        current_sum += num

        required = current_sum - k

        if required in prefix:
            count += prefix[required]

        prefix[current_sum] = prefix.get(current_sum, 0) + 1

    return count


arr = [1, 2, 3]
k = 3

print(subarray_sum(arr, k))