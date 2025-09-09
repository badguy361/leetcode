"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
# solution 1
"""
做法:
1. 使用集合來記錄窗口中的字符
2. 使用變量 temp_ans 來記錄當前窗口的長度
3. 使用變量 ans 來記錄最長無重複子串的長度
4. 遍歷字符串，更新集合和變量
5. 返回 ans
複雜度:
- 時間複雜度: O(n2)
- 空間複雜度: O(n)
"""
s = " "
left = 0
right = 0
temp_ans = 0
ans = 0
while right < len(s):
    nums_set = set(s[left:right])
    if s[right] not in nums_set:
        right += 1
        temp_ans += 1
        ans = max(ans,temp_ans)
    else:
        left += 1
        temp_ans = right - left + 1
    ans = max(ans, temp_ans)
print(ans)

# solution 2
"""
做法:
1. 使用字典來記錄每個字符最後出現的位置
2. 使用變量 max_length 來記錄最長無重複子串的長度
3. 使用變量 start 來記錄當前窗口的起始位置
4. 遍歷字符串，更新字典和變量
5. 返回 max_length
"""
if not s:
    print(0)

# 使用字典來記錄每個字符最後出現的位置
char_index = {}
max_length = 0
start = 0

for i, char in enumerate(s):
    # 如果字符已經在當前窗口中出現過，更新起始位置
    if char in char_index and char_index[char] >= start:
        start = char_index[char] + 1
    # 更新字符的最新位置
    char_index[char] = i
    # 計算當前窗口長度並更新最大長度
    current_length = i - start + 1
    max_length = max(max_length, current_length)

print(max_length)
