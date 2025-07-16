class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            nums = list(s)
            slow = 0
            for fast in range(len(nums)):
                if nums[fast] != '#':
                    nums[slow] = nums[fast]
                    slow += 1
                else:
                    if slow > 0:
                        slow -= 1
            return ''.join(nums[:slow])
        return process_string(s) == process_string(t)