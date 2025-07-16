from typing import List

# 暴力
class Solution_1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num * num)
        result.sort()
        return result
    
# 双指针
class Solution_2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
        return result