"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


def longestRChar(s, k):
    lp = 0
    rp = 0
    char_freq = {}
    maxc = 0
    longest = 1
    while rp < len(s):
        if s[rp] in char_freq:
            char_freq[s[rp]] += 1
        else:
            char_freq[s[rp]] = 1
        rp += 1
        if (rp - lp) - maxc > k:
            char_freq[s[lp]] -= 1
            lp += 1
        maxc = max(char_freq.values())
        longest = max(longest, rp - lp+1)
    return longest


print(longestRChar("AABABBA", 1))
