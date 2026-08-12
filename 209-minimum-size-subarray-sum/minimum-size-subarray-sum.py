class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        n = len(nums)
        summ = 0
        import math
        res = math.inf
        while (high<n):
            summ = summ + nums[high]
            while(summ>=target):
                lenn = high - low + 1
                res = min(res, lenn)
                summ = summ - nums[low]
                low+=1

            high+=1
        if res == math.inf:
            return 0
        else:
            return res

        