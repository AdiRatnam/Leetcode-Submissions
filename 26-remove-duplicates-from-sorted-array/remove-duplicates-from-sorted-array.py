class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        i = 0
        j = 1
        while (j < n):
            if nums[i] == nums[j]:
                j+=1

            else:
                i+=1
                nums[i] = nums[j]
                k+=1
                j+=1
        
        return k




        
        