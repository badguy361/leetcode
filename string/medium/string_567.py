"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

# Test Case
s1 = "ab"
s2 = "eidbaooo"

# s1 = "ab"
# s2 = "eidboaoo"

# s1 = "abc"
# s2 = "cba"

# soluton 1
"""
做法: 使用window的概念，遍歷s2，並使用s1_table來比對是否包含s1的組成元素
複雜度: O(n*k)
"""
from collections import Counter
left = 0
right = left + len(s1)
count_s1 = Counter(ch for ch in s1 if ch.isalpha())
while right <= len(s2):
    count_s2_window = Counter(ch for ch in s2[left:right] if ch.isalpha())
    if count_s2_window == count_s1:
        print(True)
        break
    left += 1
    right = left + len(s1)
print(False)

# solution 2:
"""
做法: 使用window的概念，遍歷s2，並使用s1_table來比對是否包含s1的組成元素
複雜度: O(n)
"""
def count_char(string, table):
    for char in string:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    return table

s1_table = {}
s1_table = count_char(s1, s1_table)

window = len(s1)
flag = False
for i in range(len(s2)-window+1):
    s2_table = {}
    s2_table = count_char(s2[i:i+window], s2_table)
    if s2_table == s1_table:
        flag = True
        break
    flag = False
print(flag)
