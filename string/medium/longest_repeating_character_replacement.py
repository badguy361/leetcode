"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k.
You can choose any character of the string and change it to any other character.
You can perform this operation at most k times.
Return the length of the longest substring containing 
the same letter after performing the operation.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""
# Test Case
s = "ABAB"
k = 2

# solution 1
"""
做法:
slide window
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(1)
"""
left = 0
max_count = 0
ans = 0
count = {}
for right in range(len(s)):
    if s[right] not in count:
        count[s[right]] = 1
    else:
        count[s[right]] += 1
    max_count = max(max_count, count[s[right]])
    while (right - left + 1) - max_count > k:
        count[s[left]] -= 1
        left += 1
    ans = max(ans, right - left + 1)
print(ans)
