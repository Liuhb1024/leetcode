# 二分查找

704. 二分查找 - 力扣（LeetCode）

## 思路

这道题的前提是有序数组，并且题目中还强调没有重复元素。
这也是使用二分的前提之一，因为一旦有重复元素，使用二分返回的元素下标就不是唯一的。

并且二分涉及的边界问题有很多，主要是因为对区间的定义没有想明白，区间的定义就是不变量

## 关于二分

对于区间的定义一般分为两种：
- 左闭右闭 [left, right]
- 左闭右开 [left, right)

### 1. 左闭右闭 [left, right]

将定义的 target 放在左闭右闭的区间中

- while (left <= right) 要使用 <= ，因为left == right是有意义的，所以使用 <=
- if (nums[middle] > target)  right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，那么接下来要查找的左区间结束下标位置就是 middle - 1

```python
class Solution:
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
```

### 2. 左闭右开 [left, right)

如果说定义 target 是在一个在左闭右开的区间里，也就是[left, right) ，那么二分法的边界处理方式则截然不同。

有如下两点：
- while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
- if (nums[middle] > target) right 更新为 middle，因为当前nums[middle]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，所以right更新为middle，即：下一个查询区间不会去比较nums[middle]

```python
class Solution:
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
