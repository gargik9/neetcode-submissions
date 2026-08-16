class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position,speed))

        cars = sorted(cars, reverse="True")

        prev_time = 0

        no_fleets = 0

        for pos, spd in cars:

            tm = (target - pos)/spd

            if tm>prev_time:

                no_fleets+=1

                prev_time = tm

        return no_fleets


        