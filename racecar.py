class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,0,1))
        count = 0
        seen = set((0,0,1))
        while queue:
            count, pos, speed = queue.popleft()
            if pos == target:
                return count
            opt1 = (count+1,pos + speed, 2 * speed)
            s = -1 if speed > 0 else 1
            opt2 = (count+1,pos, s)
            if opt1 not in seen and 0 <= pos+speed <= 2*target:
                seen.add(opt1)
                queue.append(opt1)
            if opt2 not in seen and 0 <= pos <= 2*target:
                seen.add(opt2)
                queue.append(opt2)


