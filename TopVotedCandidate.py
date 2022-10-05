class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        count = {}
        self.ans = [0] * len(persons)
        max_ = (float('-inf'),-1)
        for i,person in enumerate(persons):
            count[person] = count.get(person,0) + 1
            if count[person] >= max_[0]:
                max_ = (count[person],person)
            self.ans[i] = max_[1]
      
    def q(self, t: int) -> int:
        i = bisect_right(self.times,t)-1
        return self.ans[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
