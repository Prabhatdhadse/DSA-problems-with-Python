# nums = [1,1,1,2,3,4,4,5,7,9,9,10]

# n = len(nums)
# freq_map = {}

# for i in range(0,n):
#     freq_map[nums[i]] = 0
# j = 0
# for k in freq_map:
#     nums[j] = k
#     j +=1
# print(freq_map)



from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        freq_map = {}

        for i in range(0,n):
            freq_map[nums[i]] = 0

        j = 0
        for k in freq_map:
            nums[j] = k
            j += 1

        return j

obj = Solution()
print(obj.removeDuplicates([1,1,2]))
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    
        