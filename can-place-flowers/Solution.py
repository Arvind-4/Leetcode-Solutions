// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, prev = 0, 0
        for current in flowerbed:
            if current == 1:
                if prev == 1:
                    count -= 1
                prev = 1
            else:
                if prev == 1:
                    prev = 0 
                else:
                    count += 1
                    prev = 1
        return count >= n



