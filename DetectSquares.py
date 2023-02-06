class DetectSquares:
    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.points[(x,y)] = self.points.get((x,y),0) + 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point[0], point[1]
        for x2, y2 in self.points:
            if abs(x1 - x2) > 0 and abs(x1 - x2) == abs(y1 - y2) and (x1,y2) in self.points and (x2,y1) in self.points:
                    count += self.points[(x2,y2)] * self.points[(x1,y2)] * self.points[(x2,y1)]
        return count
    
