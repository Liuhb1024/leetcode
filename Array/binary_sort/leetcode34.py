from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 寻找左边界
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            res  = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        res = mid
                    right = mid - 1
            return res

        # 寻找右边界
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        res = mid
                    left = mid + 1
            return res

        leftIndex = findLeft(nums, target)
        rightIndex = findRight(nums, target)
        return [leftIndex, rightIndex]