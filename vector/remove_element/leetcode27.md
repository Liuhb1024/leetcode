# LeetCode 27. Remove Element 解法分析

## 问题描述
给定一个数组 nums 和一个值 val，原地移除所有数值等于 val 的元素，并返回移除后数组的新长度。要求：
- 必须原地修改数组
- 不需要考虑数组中超出新长度后面的元素

## 核心算法：快慢指针法

### 算法原理
使用双指针技巧：
- 快指针(fast)：遍历数组，寻找保留元素
- 慢指针(slow)：标记下一个保留元素应该存放的位置

### 代码实现
```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
```

## 代码解析

### 指针初始化
```python
fast = 0
slow = 0
```
- 两个指针都从数组起始位置开始

### 主循环
```python
while fast < len(nums):
    if nums[fast] != val:
        nums[slow] = nums[fast]
        slow += 1
    fast += 1
```
1. 快指针遍历每个元素
2. 当遇到不等于val的元素时：
   - 将其复制到慢指针位置
   - 慢指针前进
3. 无论是否复制，快指针都前进

### 返回结果
```python
return slow
```
- slow指针的位置即为新数组长度

## 复杂度分析
- 时间复杂度：O(n) - 只需遍历数组一次
- 空间复杂度：O(1) - 只使用了常数空间

## 关键点解释
1. 原地修改：直接在原数组上操作，不创建新数组
2. 元素覆盖：通过快慢指针实现高效元素移动
3. 新长度：慢指针最终位置即为新数组长度
4. 元素顺序：保留元素的相对顺序保持不变

## 优缺点
优点：
- 高效，只需一次遍历
- 空间复杂度最优
- 保留元素顺序

缺点：
- 需要理解双指针概念
- 对不熟悉指针操作的开发者可能较难理解

## 应用场景
- 需要原地修改数组的情况
- 需要保持元素顺序的删除操作
- 空间复杂度要求严格的场景

## 总结
快慢指针法是解决原地删除数组元素的经典方法，通过巧妙地使用两个指针实现高效操作。理解这种解法有助于掌握数组操作的核心技巧。
