def doSearch(array, targetValue):
    minVal = 0;
    maxVal = len(array) - 1;

    while minVal <= maxVal:
        mid = minVal + (maxVal - minVal) // 2
        if array[mid]  == targetValue:
            return mid
        elif array[mid] > targetValue:
            maxVal = mid - 1
        else:
            minVal = mid + 1
		
    return -1

print(doSearch([1,2,3,4,5,6,7,8,9,10], 5))
print(doSearch([1,2,3,4,5,6,7,8,9,10], 7))
print(doSearch([1,2,3,4,5,6,7,8,9,10], 9))
print(doSearch([1,2,3,4,5,6,7,8,9,10], 10))
print(doSearch([], 9))