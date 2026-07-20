class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSerie = 0
        currentSerie = 0
        for num in nums:
            if num == 1:
                currentSerie += 1
                if currentSerie > maxSerie:
                    maxSerie = currentSerie
            else:
                currentSerie = 0
        return maxSerie