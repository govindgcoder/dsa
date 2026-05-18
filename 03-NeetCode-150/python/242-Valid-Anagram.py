"""Given two strings s and t, return true if t is an of s, and false otherwise."""

s = "car"
t = "rac"


def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    return False


print(isAnagram(s, t))
