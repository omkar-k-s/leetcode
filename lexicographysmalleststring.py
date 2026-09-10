def smallest_string(s):
    for i in range (len(s)-1):
        if s[i]>s[i+1]:
            return s[:i]+s[i+1:]
    return s[:-1]
