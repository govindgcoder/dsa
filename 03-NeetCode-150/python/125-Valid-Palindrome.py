"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


# def isValid(s):
#     s = "".join(i.lower() if i.isalnum() else "" for i in s)
#     return s == s[::-1]

def isValid(s):
    fp,lp=0,len(s)-1
    while fp<=lp:
        if not s[fp].isalnum():
            fp+=1
            continue
        if not s[lp].isalnum():
            lp-=1
            continue
        if s[fp].lower()!=s[lp].lower():
            return False
        fp+=1
        lp-=1
    return True

print(isValid("A man, a plan, a canal: Panama"))
