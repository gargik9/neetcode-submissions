class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position,speed))

        prev_time = 0

        fleets = 0

        cars = sorted(cars, reverse = "True")

        for car in cars:

            pos = car[0]
            spd = car[1]

            tm = (target - pos)/spd

            if tm>prev_time:

                fleets+=1

                prev_time = tm

        return fleets

        