# LeetCode 283. Move Zeroes

## 问题描述
给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

## 算法思路
使用双指针（快慢指针）技术：
1. `slow` 指针指向当前需要放置非零元素的位置
2. `fast` 指针遍历整个数组
3. 当 `nums[fast]` 不为零时，将其值复制到 `nums[slow]`，然后 `slow` 前进
4. 遍历完成后，所有非零元素都已移动到数组前部，`slow` 指针之后的位置全部置零

## 时间复杂度
- O(n): 需要遍历数组两次（一次移动非零元素，一次填充零）
- 实际上可以认为是 O(2n)，但常数因子可以忽略

## 空间复杂度
- O(1): 原地操作，只使用了常数个额外空间

## 代码逐步解释
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0  # 初始化慢指针
        
        # 第一次遍历：移动所有非零元素到前面
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]  # 复制非零元素
                slow += 1  # 慢指针前进
        
        # 第二次遍历：将剩余位置填充为零
        for i in range(slow, len(nums)):
            nums[i] = 0
```

## 优化思考
1. 可以优化为单次遍历吗？
   - 可以，但会牺牲代码可读性
   - 方法是当遇到非零元素时，与慢指针位置交换
2. 为什么选择这种实现？
   - 保持非零元素原始顺序
   - 写操作最少（每个非零元素只写一次）

## 类似问题
- LeetCode 26. Remove Duplicates from Sorted Array
- LeetCode 27. Remove Element
