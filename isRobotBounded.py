class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        points = (0,0)
        direction = (0,1)
        for instruction in instructions:
            if instruction == 'G':
                points = (points[0]+direction[0],points[1]+direction[1])
            elif instruction == 'L':
                if direction[0] == 1:
                    direction = (0,1)
                elif direction[0] == -1:
                    direction = (0,-1)
                elif direction[1] == 1:
                    direction = (-1,0)
                elif direction[1] == -1:
                    direction = (1,0)
            else:
                if direction[0] == 1:
                    direction = (0,-1)
                elif direction[0] == -1:
                    direction = (0,1)
                elif direction[1] == 1:
                    direction = (1,0)
                elif direction[1] == -1:
                    direction = (-1,0)
        return points == (0,0) or direction[1] != 1
