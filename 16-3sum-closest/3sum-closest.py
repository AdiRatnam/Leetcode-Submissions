class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        min_diff = math.inf
        cs = 0
        for i in range(n-2):
            if (i<0 and nums[i] == nums[i-1]):
                continue
            else:
                left = i+1
                right = n-1

                while(left<right):
                    sum = nums[i] + nums[left] + nums[right]

                    diff = abs(sum - target)
                    if diff < min_diff:
                        min_diff = diff
                        cs = sum

                    if sum == target:
                        return target

                    if sum < target:
                        left+=1

                    else:
                        right-=1

        return cs



        