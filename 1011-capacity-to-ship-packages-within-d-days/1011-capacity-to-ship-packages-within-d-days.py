class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validWeight(capacity):
            daysNeeded, totalWeight = 1, 0
            for weight in weights:
                totalWeight += weight
                if totalWeight > capacity:
                    totalWeight = weight
                    daysNeeded += 1
            return daysNeeded <= days

        minCapacity, maxCapacity = max(weights), sum(weights)
        ans = 0
        while minCapacity <= maxCapacity:
            midWeight = (minCapacity + maxCapacity) // 2
            if validWeight(midWeight):
                ans = midWeight
                maxCapacity = midWeight - 1
            else:
                minCapacity = midWeight + 1
        return ans
      