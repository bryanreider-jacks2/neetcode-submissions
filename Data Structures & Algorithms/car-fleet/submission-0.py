class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > slowest_time:
                fleets += 1
                slowest_time = time
        
        return fleets



"""
Input: target = 10, position = [1,4,3,2], speed = [3,2,7,1]

time[i] = (target - position[i]) / speed[i]

cars = sorted(zip(position, speed), reverse=True)

cars = [(4,2), (3,7), (2,1), (1,3)]

times = [3,1,8,3]

fleets = 0
slowest_time = 0
"""