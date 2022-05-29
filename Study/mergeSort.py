# Method - 1
# Time Complexity - O(n)
# Space Complexity - O(n.log(n))

def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:] 
    return mergerSortArray(mergeSort(leftHalf), mergeSort(rightHalf))

def mergerSortArray(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) * len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    # Sorting remaining elements in left/right halves
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        j += 1
    
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1

    return sortedArray
    
# Method 2
# Time - O(n.log(n))
# Space - O(n)

def mergetSort(array):
    if len(array) == 1:
        return array
    auxiliaryArray = array[:]
    mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
    return array

def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx
    i = startIdx
    j = middleIdx + 1
    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1

    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1

    while j < endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1

    


