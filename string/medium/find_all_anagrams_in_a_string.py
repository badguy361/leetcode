"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams
in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""
# solution 1:
"""
做法:
1. 使用 Counter 計算 p 中每個字符的頻率
2. 遍歷 s，對於每個位置，檢查 s 中以該位置開始的長度為 p 的子串是否與 p 的頻率相同
3. 如果相同，將該位置加入結果列表
4. 返回結果列表
複雜度:
- 時間複雜度: O(n*m)，其中 n 是 s 的長度，m 是 p 的長度。每次檢查子串需要 O(m) 時間，總共需要檢查 n-m+1 次。
"""
from collections import Counter
from typing import List
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        ans = []

        p_length = len(p)
        s_length = len(s)
        for index in range(s_length):
            if index <= s_length-p_length:
                current_window = Counter(s[index:index+p_length])
                if current_window == target:
                    ans.append(index)
        return ans

# solution 2: sliding window
"""
做法:
1. 使用 Counter 計算 p 中每個字符的頻率
2. 遍歷 s，對於每個位置，檢查 s 中以該位置開始的長度為 p 的子串是否與 p 的頻率相同
3. 如果相同，將該位置加入結果列表
4. 返回結果列表
複雜度:
- 時間複雜度: O(n)，其中 n 是 s 的長度。每次檢查子串需要 O(1) 時間，總共需要檢查 n 次。
"""
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        ans = []
        p_counter = Counter(p)
        s_counter = Counter()

        for i in range(s_len):
            s_counter[s[i]]+=1
            if i >= p_len:
                left_char = s[i - p_len]
                if s_counter[left_char] == 1:
                    del s_counter[left_char]
                else:
                    s_counter[left_char]-=1
            if s_counter == p_counter:
                ans.append(i-p_len+1)
        return ans
