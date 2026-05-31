class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #value -> index
        for i,num in enumerate(nums):
            answer = target - num #needed value
            if answer in seen: #check if we already saw it
                return [seen[answer], i]
            seen[num] = i  #store value with index
