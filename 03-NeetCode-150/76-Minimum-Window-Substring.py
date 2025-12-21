"""
Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
    
Solution:

So we gotta find the minimum length substring, that contains all of the elements of the give small string in the large string.

A sliding window is to be used to check through the array - better T.C

A dictionary can be kept to keep track if the current window has the characters of the small string.

dictionary can be updated each time the lp and fp moves.

when the whole dictionary is true, store the current lp and rp if the previous rp and rp is a longer window, if it was empty just store the new window.

return the final stored lp and rp to give the required minimum window substring. 

lp needs to be incremented while the dictionary is true

We could maintain the count in the dictionary, and have another variable to track have count and when that is equal to need count the window is valid, however this requires logic to know if the current pointer variable in the current dictionary has a value greater or equal to the ideal dictionary, decrement need count is it is and increment need count if it is not when leaving the lp. 

Implementation logic.

dict - refDict, currentDict=all of refDict but values of 0
int - need=number of unique chars of ref String, have=0, lp=0, rp=0, minLp=0, minRp = length of large string

loop:
	check if s[rp] is in refDict: 
		currentDict[rp]+=1
		if currentDict[rp]==refDict:
			have+=1
	while have = need:
		if(minRp-minLp>rp-lp):
			minRp = rp
			minLp = lp
		check if s[lp] in refDict:
			currentDict[lp]-=1
			if currentDict[lp]<refDict:
				have-=1
		lp+=1
	increment rp
	return "" if lp==rps else s[lp:rp+1]
"""

from math import inf


def minWindowSubString(s, t):
	refSet = set(t)
	refDict = {k: 0 for k in t}
	currDict = {k: 0 for k in t}
	# to make the reference dict and need count
	need = len(refSet)
	for i in t:
		refDict[i]+=1
	# for the checking
	lp = 0
	rp = 0
	# initial window must be the largest to make minwindow<currwindow condition work.
	minLp = 0
	minRp = float("inf")
	have = 0
	# main loop for sliding window
	while(rp<len(s)):
		# update dictionaries based on lp
		if s[rp] in refDict:
			currDict[s[rp]]+=1
			if currDict[s[rp]]==refDict[s[rp]]:
				have+=1
		while have == need and lp<=rp:
			# shorten window while it is valid
			if(minRp-minLp>rp-lp):
				minRp = rp
				minLp = lp
			if s[lp] in refDict:
				currDict[s[lp]]-=1
				if currDict[s[lp]]<refDict[s[lp]]:
					have-=1
			lp+=1
		rp+=1
	# return the minimum window
	return "" if minRp==float("inf") else s[minLp:minRp+1]
	
print(minWindowSubString(s = "a", t = "a"))