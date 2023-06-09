// https://leetcode.com/problems/sort-array-by-parity-ii

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else: odd.append(nums[i])
        for i in range(0, len(nums), 2):
            nums[i] = even[j]
            nums[i + 1] = odd[j]
            j += 1
        return nums