"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

# solution 1
"""
做法:
1. 使用字典來記錄每個字符最後出現的位置
2. 使用變量 max_length 來記錄最長無重複子串的長度
3. 使用變量 start 來記錄當前窗口的起始位置
4. 遍歷字符串，更新字典和變量
5. 返回 max_length
複雜度:
- 時間複雜度: 每個字串排序：O(k log k)，k 為字串長度
- 總計：O(n * k log k)，n 為字串數量
"""
from collections import defaultdict
ans = defaultdict(list)
strs = ["eat","tea","tan","ate","nat","bat"]
for s in strs:
    key = ''.join(sorted(s))
    ans[key].append(s)
print(list(ans.values()))
