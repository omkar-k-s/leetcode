from collections import Counter

def min_window(s, t):

    need = Counter(t)
    window = {}

    left = 0
    formed = 0

    required = len(need)

    min_length = float('inf')
    answer = ""

    for right in range(len(s)):

        char = s[right]

        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1

        while formed == required:

            if right - left + 1 < min_length:
                min_length = right - left + 1
                answer = s[left:right + 1]

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return answer


s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s, t))

