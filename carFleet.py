class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i],speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x:x[0],reverse=True)
        fleet = [cars[0]]
        for i in range(1,len(cars)):
            if (target-fleet[-1][0])/fleet[-1][1] < (target-cars[i][0])/cars[i][1]:
                fleet.append(cars[i])
        return len(fleet)
