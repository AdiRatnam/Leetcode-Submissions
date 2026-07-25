class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        j = 2
        k = 2
        while( j < len(nums)):
            if nums[j] == nums[i-2]:
                j+=1
                
            else:
                nums[i] = nums[j]
                j+=1
                i+=1
                k+=1

        return k



        