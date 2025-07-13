# LeetCode 69. Sqrt(x) 解法分析

## 问题描述
实现 int sqrt(int x) 函数，计算并返回 x 的平方根，其中 x 是非负整数。由于返回类型是整数，结果只保留整数部分，小数部分将被舍去。

## 解法思路：二分查找法
利用二分查找在可能的整数范围内寻找最大的整数 mid，使得 mid² ≤ x。

### 数学原理
1. 平方根函数的性质：对于 x ≥ 0，√x 的值域是 [0, x]
2. 对于 x ≥ 2，√x 的值域可以缩小到 [1, x/2]，因为：
   - (x/2)² = x²/4 ≥ x 当 x ≥ 4 时
   - 因此搜索范围可以优化为 [1, x//2]

## 代码实现
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (right + left) // 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt < x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans
```

## 代码解析

### 边界条件处理
```python
if x < 2:
    return x
```
- 处理 x = 0 或 1 的情况，直接返回 x
- 因为 0² = 0，1² = 1

### 初始化搜索范围
```python 
left, right = 1, x // 2
```
- 根据数学原理优化搜索范围
- 对于 x ≥ 2，√x 的最大可能值是 x//2

### 二分查找核心逻辑
```python
while left <= right:
    mid = (right + left) // 2
    sqrt = mid * mid
    if sqrt == x:
        return mid
    elif sqrt < x:
        left = mid + 1
        ans = mid  # 记录当前可能解
    else:
        right = mid - 1
```
1. 计算中间值 mid
2. 比较 mid² 与 x：
   - 相等：直接返回 mid
   - mid² < x：搜索右半部分，并记录当前 mid 为可能解
   - mid² > x：搜索左半部分
3. 循环结束时，ans 保存着最大的整数满足 ans² ≤ x

## 复杂度分析
- 时间复杂度：O(log n) - 标准的二分查找复杂度
- 空间复杂度：O(1) - 只使用了常数空间

## 关键点解释
1. 搜索范围优化：将 right 初始化为 x//2 而非 x，减少搜索次数
2. ans 变量的作用：记录最后一个满足 mid² < x 的 mid 值
3. 循环条件 left <= right：确保能处理所有情况
4. 整数溢出问题：Python 不需要考虑，但其他语言需要注意 (right + left) 可能溢出

## 优缺点
优点：
- 效率高，时间复杂度为 O(log n)
- 代码简洁明了
- 搜索范围优化减少了迭代次数

缺点：
- 对于非常大的 x 值，mid*mid 可能溢出（在Python中不是问题）
- 需要理解二分查找的变种应用

## 总结
这种解法巧妙地应用了二分查找来求解平方根的整数部分，通过数学原理优化了搜索范围，是效率与简洁性兼具的优秀解法。理解这种解法有助于掌握二分查找的变种应用场景。
