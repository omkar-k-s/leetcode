def three_sum(arr):
    n=len(arr)
    ans = float('-inf')
    for i in range(n):
        for j in range(i+2, n):
            for k in range(j+2, n):
                ans = max(ans, arr[i] + arr[j] + arr[k])
    return ans