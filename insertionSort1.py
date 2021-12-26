
def insertionSort1(n, arr):
    for i in range(1,len(arr)):
        currentElement = arr[i]
        j = i - 1
        while j >= 0 and currentElement < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            for i in arr:
                print(i,end=" ")
            print()
        if arr[j+1] != currentElement:
            arr[j+1] = currentElement 
            for i in arr:
                print(i,end=" ")
            print()
        arr[j+1] = currentElement
        