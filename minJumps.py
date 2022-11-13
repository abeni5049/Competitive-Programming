class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indices = defaultdict(list)
        for i,num in enumerate(arr):
            indices[num].append(i)
        
        level = [0]
        visited = {0}
        min_jumps = 0
        while level:
            temp = []
            for index in level:
                if index == len(arr)-1:
                    return min_jumps
                while indices[arr[index]]:
                    i = indices[arr[index]].pop()
                    if i not in visited:
                        temp.append(i)
                        visited.add(i)
                if index+1 not in visited:
                    temp.append(index+1)
                    visited.add(index+1)
                if index-1 >=0 and index-1 not in visited:
                    temp.append(index-1)
                    visited.add(index-1)
            level = temp
            min_jumps += 1
        return min_jumps
                
