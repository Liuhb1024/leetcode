class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        def mySort(num):
            left, right = 1, num // 2
            while left <= right:
                mid = (left + right) // 2
                sqrt = mid * mid
                if sqrt == num:
                    return mid
                elif sqrt < num:
                    left = mid + 1
                    ans = mid
                else:
                    right = mid - 1
            return ans
        result = mySort(num)
        if num == result * result: return True
        else: return False