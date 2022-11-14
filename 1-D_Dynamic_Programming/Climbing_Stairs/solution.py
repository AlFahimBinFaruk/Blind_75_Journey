class Solution:
    # Time O(N-1) | Space O(1)
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one    