class Solution: 
    def select(self, arr, i):
        minIndex = 0
        for i in range(1,i):
            if arr[i] < arr[minIndex]:
                minIndex = i
        return minIndex
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minIndex = self.select(arr[i:n],n-i) + i
            arr[i],arr[minIndex] = arr[minIndex] , arr[i]