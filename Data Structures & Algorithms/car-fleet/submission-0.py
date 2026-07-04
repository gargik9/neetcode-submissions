class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars = list(zip(position,speed))
        
        # Sort cars from closest to target -> farthest
        cars.sort(reverse=True)

        fleets = 0
        last_time = 0

        # Process cars from front to back
        for pos, spd in cars:

            # Time needed for this car to reach the target
            time = (target - pos) / spd

            # If this car takes longer than the fleet ahead,
            # it cannot catch up, so it forms a new fleet.
            if time > last_time:
                fleets += 1
                last_time = time

            # Otherwise, this car catches the fleet ahead,
            # so we don't create a new fleet.

        return fleets