"""
76. Minimum Window Substring
"""
# solution 1
"""
做法: sliding window
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(1)
"""
from collections import Counter

def minWindow(s: str, t: str) -> str:
    l,r = 0,0
    count_t = Counter(t)
    count_window = {}
    have = 0
    criteria = len(count_t)
    min_len = float("inf")
    ans = ""

    while r < len(s):
        count_window[s[r]] = count_window.get(s[r],0) + 1
        if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
            have += 1

        while have == criteria:
            ans_len = r - l + 1
            if ans_len < min_len:
                ans = s[l:r+1]
                min_len = ans_len

            count_window[s[l]] -= 1
            if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
        r += 1
    return ans
