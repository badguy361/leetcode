"""
767. Reorganize String
Given a string s, rearrange the characters of s so that any two 
adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""
# solution 1
class Solution:
    def reorganizeString(self, s: str) -> str:
        def count(s, key):
            num = 0
            for i in s:
                if i == key:
                    num += 1

            return num

        def check(num, exceed_cond):
            if num <= exceed_cond:
                return num
            return False

        def process(statics):
            ans = []
            while statics:
                sorted_list = sorted(statics.items(), key=lambda item: item[1]) # sort dict by value
                top_key = sorted_list[-1][0]
                top_value = sorted_list[-1][1]
                if len(sorted_list) > 1:
                    second_key = sorted_list[-2][0]
                    second_value = sorted_list[-2][1]
                    ans.extend(top_key)
                    ans.extend(second_key)
                    statics[top_key] = top_value - 1
                    statics[second_key] = second_value - 1
                else:
                    ans.extend(top_key)
                    statics[top_key] = top_value - 1

                statics = {k: v for k, v in statics.items() if v != 0} # get not zero dict
            return ans

        exceed_cond = (len(s)-1)/2 + 1
        s_key = set(s)
        stack = {}
        for key in s_key:
            tmp = count(s, key)
            num = check(tmp, exceed_cond)
            if num:
                stack[key] = num
            else:
                return ''
        ans = process(stack)
        return ''.join(ans)
