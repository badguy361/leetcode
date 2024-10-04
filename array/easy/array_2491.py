"""
2491. You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
 

Constraints:

2 <= skill.length <= 105
skill.length is even.
1 <= skill[i] <= 1000

"""

# solution 1:
"""
做法 : 遍歷所有可能的組合
複雜度 : O(n^2) (用list或array做查詢的複雜度會是O(n)，HashMap的複雜度會是O(1))
"""
# import numpy as np
# skill =[2,3,4,2,5,5]
# target = sum(skill)/(len(skill)/2)
# obj_set = np.array([])
# value = int(0)
# for ski in skill:
#     obj = target - ski
#     if obj in obj_set:
#         tmp = obj * ski
#         value += tmp
#         obj_set = np.delete(obj_set,np.where(obj_set == obj)[0][0])
#     else:
#         obj_set = np.append(obj_set,ski)

# if len(obj_set) != 0:
#     print("value: -1")
# else:
#     print("value:",value)

# solution 2:
"""
做法 : 排序後遍歷
複雜度 : O(nlogn)
"""
skill = [1,1,2,3]
skill.sort() # python內建的Timsort複雜度是O(nlogn)
value = 0
target = sum(skill)/(len(skill)/2)
for i in range(len(skill)//2):
    if skill[i] + skill[-i-1] != target:
        print(-1)
    else:
        tmp = skill[i] * skill[-i-1]
        value += tmp

