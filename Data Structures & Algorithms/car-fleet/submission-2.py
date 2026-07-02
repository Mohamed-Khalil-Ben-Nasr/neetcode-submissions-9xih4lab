class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = []
        n = len(position)
        for i in range(n):
            sortedCars.append([position[i], speed[i]])
        # o(nlogn) time
        sortedCars.sort(key = lambda x: x[0])
        print(sortedCars)
        # O(n) time
        # O(1) space
        currentFleetTime = 0
        res = 0
        for i in range(n-1,-1,-1):
            curPos, curSpeed = sortedCars[i]
            timeToTarget = (target - curPos) / curSpeed
            if timeToTarget > currentFleetTime:
                res += 1
                currentFleetTime = timeToTarget
                
        return res
