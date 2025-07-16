# LeetCode 844. Backspace String Compare

## 问题描述
给定两个字符串 `s` 和 `t`，当它们分别被输入到空文本编辑器后，判断两者是否相等。'#' 代表退格字符。

示例 1：
```
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"
```

示例 2：
```
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""
```

## 算法思路
使用双指针技术处理字符串：
1. 定义内部函数 `process_string` 处理单个字符串
2. 使用快慢指针遍历字符串：
   - 快指针(`fast`)遍历每个字符
   - 慢指针(`slow`)指向当前有效字符的位置
3. 遇到普通字符时，将其复制到慢指针位置，慢指针前进
4. 遇到退格符(`#`)时，慢指针后退（模拟删除操作）
5. 最后比较两个处理后的字符串

## 复杂度分析
- 时间复杂度：O(n + m)，其中n和m分别是字符串s和t的长度
- 空间复杂度：O(n + m)，需要将字符串转换为列表进行处理

## 代码逐步解释
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            nums = list(s)  # 转换为列表便于修改
            slow = 0  # 慢指针初始化
            
            # 快指针遍历整个字符串
            for fast in range(len(nums)):
                if nums[fast] != '#':  # 普通字符
                    nums[slow] = nums[fast]
                    slow += 1
                else:  # 退格符
                    if slow > 0:  # 确保慢指针不越界
                        slow -= 1  # 模拟删除操作
            return ''.join(nums[:slow])  # 返回处理后的字符串
        
        # 比较两个字符串处理后的结果
        return process_string(s) == process_string(t)
```

## 关键点分析
1. **双指针技巧**：
   - 快指针负责遍历
   - 慢指针维护有效字符位置

2. **退格处理**：
   - 遇到`#`时慢指针回退
   - 需要检查慢指针是否大于0避免越界

3. **字符串转换**：
   - Python字符串不可变，需要先转为列表
   - 最后再转回字符串进行比较

## 边界条件
1. 连续多个退格符：`"a###b"` → `"b"`
2. 退格符在开头：`"#ab"` → `"ab"`
3. 空字符串输入：`""` 和 `"#"`
4. 全是退格符：`"####"` → `""`

## 优化方向
1. **空间优化**：
   - 可以使用栈结构，但空间复杂度相同
   - 可以尝试从后向前遍历的O(1)空间解法

2. **提前终止**：
   - 处理过程中发现结果不可能相同时可提前返回

## 类似问题
- LeetCode 1047. Remove All Adjacent Duplicates In String
- LeetCode 1209. Remove All Adjacent Duplicates in String II
- LeetCode 1544. Make The String Great
