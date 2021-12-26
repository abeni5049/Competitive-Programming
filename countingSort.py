def countingSort(arr):
    frequency = [0]*100
    for i in range(len(arr)):
            frequency[arr[i]] += 1
    return frequency