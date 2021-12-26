class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][len(arr[i])-1] < arr[j][len(arr[j])-1]:
                    arr[i],arr[j] = arr[j],arr[i]
        
        for i in range(len(arr)):
            lastCharacter = arr[i][len(arr[i])-1]
            arr[i] = arr[i].replace(lastCharacter,"")
            
        str = ""
        for i in range(len(arr)):
            if i == len(arr)-1:
                str += arr[i]
                break
            str += arr[i] + " "
            
        return str