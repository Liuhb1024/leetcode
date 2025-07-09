# 二分查找
class Solution_1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while(left <= right):
            middle = left + (right - left) // 2 #避免整数溢出
            if nums[middle] > target :
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

class Solution_2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) # 定义target在左闭右开的区间里，即：[left, right)

        while(left < right):
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1