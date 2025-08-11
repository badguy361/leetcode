"""
175. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

"""
# Test Case
nums = [2,0,2,1,1,0]

from typing import List
"""
做法: quickSort
複雜度: O(nlogn)
"""
def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def quickSort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = [num for num in arr[:-1] if num < pivot]
        right = [num for num in arr[:-1] if num >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)

    # 要實現原地修改，你需要直接操作 nums 列表物件的內容
    # 使用 nums[:] = ... 進行切片賦值： 這種方法會用新列表的內容替換原始列表的所有元素，
    # 從而達到原地修改的效果。這在技術上仍然會創建一個新的列表作為右側的值，但它會將該新列表的內容「複製」回原始列表的記憶體位置。
    nums[:] = quickSort(nums)
