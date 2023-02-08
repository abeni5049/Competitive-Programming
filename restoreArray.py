class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        first = adjacentPairs[0][0]
        for num, adjs in adj.items():
            if len(adjs) == 1:
                first = num
                break
        nums = [first]
        seen = {first}
        curr = first
        while len(nums) != len(adjacentPairs)+1:
            for num in adj[curr]:
                if num not in seen:
                    seen.add(num)
                    nums.append(num)
                    curr = num
        return nums
