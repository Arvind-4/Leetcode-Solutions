// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for k, v in d.items():
            if v > int(len(nums) / 2):
                return k