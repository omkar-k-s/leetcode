s = "listen"
t = "silent"

from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)