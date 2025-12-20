"""
Given two strings s1 and s2, return true if s2 contains a of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

# So the approach is prolly to slide a window of size of s1 through s2
# ab in eidbaooo
# ab !- ei
# ab !- id
# ab !- db
# ab -- ba
# return true
# ab in eidboaoo
# ab !- ei
# ab !- id
# ab !- db
# ab !- bo
# --> return false
# 
# We can use a frequency dict to speed up look up 
# pythonic comparison of dicts

def checkInclusion(s1, s2):
    lp = 0
    rp = len(s1) - 1
    s1_freq = {}
    s2_freq = {}
    for i in s1:
        if i in s1_freq:
            s1_freq[i] += 1
        else:
            s1_freq[i] = 1
    for i in range(len(s1)-1):
        if s2[i] in s2_freq:
            s2_freq[s2[i]] += 1
        else:
            s2_freq[s2[i]] = 1
    while rp < len(s2):
        if s2[rp] in s2_freq:
            s2_freq[s2[rp]] += 1
        else:
            s2_freq[s2[rp]] = 1
        if s1_freq == s2_freq:
            return True
        s2_freq[s2[lp]] -= 1
        if s2_freq[s2[lp]]==0:
       		s2_freq.pop(s2[lp])
        rp += 1
        lp += 1
    return False


print(checkInclusion("ab", "eidboaaoo"))
