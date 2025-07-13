# LeetCode 34. Find First and Last Position of Element in Sorted Array 解法分析

## 问题描述
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值，返回 [-1, -1]。

## 解法思路
使用二分查找分别寻找目标值的左边界和右边界：
1. `findLeft`函数：寻找目标值的第一个出现位置（左边界）
2. `findRight`函数：寻找目标值的最后一个出现位置（右边界）
3. 组合两个函数的结果返回最终答案

## 代码实现
```python
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
```

## 函数解析

### findLeft 函数（寻找左边界）
1. 初始化左右指针
2. 当 left <= right 时循环：
   - 计算中间位置 mid
   - 如果 nums[mid] < target，搜索右半部分 (left = mid + 1)
   - 否则：
     - 如果 nums[mid] == target，记录当前位置到 res
     - 继续搜索左半部分 (right = mid - 1)
3. 返回 res（记录的最后一次等于 target 的位置）

关键点：
- 当 nums[mid] == target 时，仍然继续向左搜索 (right = mid - 1)
- res 会记录最左边的等于 target 的位置

### findRight 函数（寻找右边界）
1. 初始化左右指针
2. 当 left <= right 时循环：
   - 计算中间位置 mid
   - 如果 nums[mid] > target，搜索左半部分 (right = mid - 1)
   - 否则：
     - 如果 nums[mid] == target，记录当前位置到 res
     - 继续搜索右半部分 (left = mid + 1)
3. 返回 res（记录的最后一次等于 target 的位置）

关键点：
- 当 nums[mid] == target 时，仍然继续向右搜索 (left = mid + 1)
- res 会记录最右边的等于 target 的位置

## 复杂度分析
- 时间复杂度：O(log n) - 执行了两次二分查找
- 空间复杂度：O(1) - 只使用了常数级别的额外空间

## 关键点解释
1. 两个二分查找的区别：
   - findLeft 在 nums[mid] == target 时继续向左搜索
   - findRight 在 nums[mid] == target 时继续向右搜索
2. `mid = left + (right - left) // 2` 防止整数溢出
3. 循环条件 `left <= right` 确保能处理所有情况

## 优缺点
优点：
- 效率高，时间复杂度为 O(log n)
- 代码结构清晰，将左右边界查找分离为两个独立函数

缺点：
- 需要执行两次二分查找
- 边界条件需要仔细处理

## 总结
这种解法巧妙地利用二分查找的特性，通过调整搜索方向来分别找到目标值的左右边界。虽然需要执行两次二分查找，但整体效率仍然很高，是解决此类问题的经典方法。
