class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max=0
        summ=0
        for i in gain:
            summ+=i
            if max<summ:
                max=summ
        return max
