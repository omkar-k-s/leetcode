def max_consecutive_ones(nums):
    count = 0
    maximum = 0

    for num in nums:
        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum

print(max_consecutive_ones([1,1,0,1,1,1]))
