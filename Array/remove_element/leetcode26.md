# LeetCode 26. Remove Duplicates from Sorted Array 详细解析

## 问题描述
给定一个已排序的数组 nums，原地删除重复出现的元素，使每个元素只出现一次，并返回新数组的长度。

## 核心算法：快慢指针法

### 算法图解
```
初始状态：[0,0,1,1,1,2,2,3,3,4]
          s f
第1步：   [0,0,1,1,1,2,2,3,3,4] (nums[f]==nums[s])
            s f  
第2步：   [0,1,1,1,1,2,2,3,3,4] (nums[f]!=nums[s], 复制并移动)
              s   f
第3步：   [0,1,1,1,1,2,2,3,3,4] (nums[f]==nums[s])
              s     f
第4步：   [0,1,2,1,1,2,2,3,3,4] (nums[f]!=nums[s], 复制并移动)
                s       f
第5步：   [0,1,2,3,1,2,2,3,3,4] (nums[f]!=nums[s], 复制并移动)
                  s         f
最终结果：[0,1,2,3,4,2,2,3,3,4] (返回slow+1=5)
```

### 代码实现
```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
```

## 详细解析

### 指针初始化
```python 
fast = 1  # 从第2个元素开始检查
slow = 0  # 指向当前唯一元素的最后位置
```
- fast指针负责遍历数组
- slow指针标记唯一序列的末尾

### 主循环逻辑
```python
while fast < len(nums):
    if nums[fast] != nums[slow]:  # 发现新元素
        slow += 1  # 扩展唯一序列
        nums[slow] = nums[fast]  # 复制新元素
    fast += 1  # 继续扫描
```
1. 比较fast和slow指向的元素
2. 当发现新元素时：
   - 移动slow指针
   - 将新元素复制到slow位置
3. fast始终前进

### 新手常见误区
1. **初始条件**：为什么fast从1开始？
   - 因为第一个元素(nums[0])必定是唯一的，无需比较

2. **返回值**：为什么返回slow+1？
   - slow是索引位置，长度需要+1
   - 例如slow=4表示有5个唯一元素(0-4)

3. **边界情况**：
   - 空数组：代码自动返回0(fast初始为1>len(nums)=0)
   - 所有元素相同：slow始终为0，返回1

4. **为什么不需要交换**：
   - 直接覆盖即可，原数据不需要保留

## 复杂度分析
- 时间复杂度：O(n) - 只需一次遍历
- 空间复杂度：O(1) - 原地修改，常数空间

## 关键点总结
1. 利用已排序数组的特性
2. slow指针维护唯一序列的边界
3. fast指针发现新元素时扩展唯一序列
4. 最终数组前slow+1个元素为去重结果

## 与其他题目对比
与LeetCode 27(Remove Element)的区别：
- 27题：删除特定值，比较nums[fast]与val
- 26题：删除重复项，比较nums[fast]与nums[slow]

## 实际应用
- 数据库去重操作
- 数据分析中的唯一值提取
- 内存优化场景
