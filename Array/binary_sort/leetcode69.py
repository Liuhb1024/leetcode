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
# Output: 4