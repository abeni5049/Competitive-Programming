class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
 
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r and l < len(people) and r > -1 :
            if people[l] + people[r] <= limit:
                l += 1
            count += 1
            r -= 1
        return count
