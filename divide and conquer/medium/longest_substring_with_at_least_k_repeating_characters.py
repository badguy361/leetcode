"""
395. Longest Substring with At Least K Repeating Characters
Given a string s and an integer k, return the length of the longest substring
of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' and 'b' are repeated 2 times.

Constraints:
1 <= s.length <= 5 * 10^4
s consists of lowercase English letters.
1 <= k <= 10^5
"""
# solution 1 (failed)
"""
思路:
1. 統計字符頻率
2. 找出頻率大於等於k的字符
3. 遍歷字符串，記錄字符頻率
4. 如果字符頻率大於等於k，記錄當前窗口長度
5. 如果字符頻率小於k，更新起始位置
6. 返回最大窗口長度
"""
from collections import Counter,defaultdict
class Solution1:
    def longestSubstring(self, s: str, k: int) -> int:
        statics = Counter(s)
        need = []
        for key,value in statics.items():
            if value >= k:
                need.append(key)

        start = 0
        ans = 0
        length = 0
        char_index = defaultdict(int)
        for i,c in enumerate(s):
            if c in need:
                char_index[c]+=1
                length = i-start+1
            else:
                start = i
                char_index = defaultdict(int)

            if any(value < k for value in char_index.values()) or not char_index:
                pass
            else:
                print(char_index)
                ans = max(length,ans)
        return ans

# solution 2
"""
做法:
1. 使用分治法，將字符串分為兩部分，分別求解
2. 遞歸求解
3. 返回最大值

測試用例 s = "bbaaacbd" 和 k = 3：
- 初始呼叫：
    count = {'b':3, 'a':3, 'c':1, 'd':1}
- 找到 c 和 d 的頻率少於 k=3，因此使用它們作為分割點。
- 分割字串：
    使用 'c' 和 'd' 分割字串，得到 ["bbaaa", "b"]
- 遞迴處理子串 "bbaaa"：
    count = {'b':2, 'a':3}
- 找到 b 的頻率少於 k=3，以 'b' 分割，得到 ["", "aaa"]
- 遞迴處理子串 ""：
    空字串，返回 0
- 遞迴處理子串 "aaa"：
    count = {'a':3}
    沒有字符的頻率少於 k=3，符合條件，返回長度 3
- 遞迴處理子串 "b"：
    count = {'b':1}
    找到 b 的頻率少於 k=3，以 'b' 分割，得到 ["", ""]
    返回 0
- 最終結果：
    比較所有子串的結果：max(0, 3, 0) = 3
    這樣就正確地識別出 "aaa" 是符合條件的最長子串，返回 3。

"""
class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        # 如果字串長度小於k，無法滿足條件
        if len(s) < k:
            return 0

        # 計算每個字符的頻率
        count = Counter(s)

        # 找出頻率小於k的字符
        for char in count:
            if count[char] < k:
                # 用這個字符分割字串，並遞迴處理各子串
                return max(self.longestSubstring(sub, k) for sub in s.split(char))

        # 如果沒有字符頻率小於k的，整個字串符合條件
        return len(s)
