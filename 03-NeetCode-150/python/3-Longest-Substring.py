"""
Given a string s, find the length of the longest

without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

"""

s = "bbbb"

def lengthOflongestSubString(s):
	lp = 0
	rp = 0
	maxc = 0
	hash = set()
	while rp<len(s):
		while(s[rp] in hash):
				hash.remove(s[lp])
				lp+=1
		hash.add(s[rp])
		maxc = max(maxc, rp-lp+1)
		rp+=1
	return maxc

print(lengthOflongestSubString(s))