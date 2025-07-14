# LeetCode 35. Search Insert Position 解法分析

## 问题描述
给定一个排序数组和一个目标值，在数组中找到目标值并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

## 解法1：线性搜索 (Solution_1)

```python
class Solution_1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
```

### 思路
- 遍历数组中的每个元素
- 当找到第一个大于或等于目标值的元素时，返回其索引
- 如果遍历完数组仍未找到，说明目标值大于所有元素，应插入到数组末尾，返回数组长度

### 复杂度分析
- 时间复杂度：O(n) - 最坏情况下需要遍历整个数组
- 空间复杂度：O(1) - 只使用了常数级别的额外空间

### 优缺点
- 优点：实现简单直观
- 缺点：对于大数组效率较低

## 解法2：二分查找 (Solution_2)

```python
class Solution_2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return right + 1
```

### 思路
1. 初始化左右指针分别指向数组首尾
2. 计算中间位置 middle
3. 比较 nums[middle] 与 target：
   - 如果相等，返回 middle
   - 如果 nums[middle] < target，搜索右半部分 (left = middle + 1)
   - 如果 nums[middle] > target，搜索左半部分 (right = middle - 1)
4. 循环结束时，如果没有找到目标值，则 right + 1 就是插入位置

### 关键点解释
- `middle = left + (right - left) // 2` 防止整数溢出
- 循环条件 `left <= right` 确保能处理所有情况
- 最终返回 `right + 1` 是因为：
  - 当循环结束时，right 指向小于 target 的最大元素
  - left 指向大于 target 的最小元素
  - 插入位置应为 left 或 right + 1

### 复杂度分析
- 时间复杂度：O(log n) - 每次迭代将搜索范围减半
- 空间复杂度：O(1) - 只使用了常数级别的额外空间

### 优缺点
- 优点：效率高，特别适合大数组
- 缺点：实现比线性搜索稍复杂

## 两种解法比较
| 比较项 | 线性搜索 | 二分查找 |
|--------|----------|----------|
| 时间复杂度 | O(n) | O(log n) |
| 空间复杂度 | O(1) | O(1) |
| 实现难度 | 简单 | 中等 |
| 适用场景 | 小数组 | 大数组或需要高效查找 |

## 总结
- 对于小规模数据，两种方法性能差异不大，可以使用更简单的线性搜索
- 对于大规模数据，二分查找明显更优
- 二分查找是更推荐的通用解法，特别是当性能是关键考虑因素时
