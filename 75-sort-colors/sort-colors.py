class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            #case 1 when mid == 0, swap low and mid , low and mid inc
            if nums[mid] == 0:
                k = nums[low]
                nums[low] = nums[mid]
                nums[mid] = k
                low+=1
                mid+=1

            # case 2 when mid == 1, best case, inc mid
            elif nums[mid] == 1:
                mid+=1

            # case 3 impt mid == 2, swap mid and high only high dec 
            elif nums[mid] == 2:
                k = nums[mid]
                nums[mid] = nums[high]
                nums[high] = k
                high -=1

        return nums

