class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        n = len(nums)
        result = []
        for i in range(0, n-2, 1):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            else:

                left = i+1
                right = n-1
                sum = - nums[i]

                while (left < right):
                    s = nums[left] + nums[right] 
                    if s == sum:
                        result.append([nums[i], nums[left], nums[right]])
                        left+=1
                        right-=1

                        while(left<n and nums[left] == nums[left-1]):
                            left+=1

                        while(right>left and nums[right] == nums[right+1]):
                            right-=1

                    elif s<sum:
                        left+=1

                    else:
                        right -=1

        return result