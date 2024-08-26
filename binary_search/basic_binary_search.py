

def binary_search(arr, search):
    high = len(arr) - 1 
    low = 0 
    while high >= low:
        mid = ((high - low) //2) + low
        midNum = arr[mid]

        if arr[high] == search:
            return high 
        elif arr[low] == search:
            return low
        elif midNum == search:
            return mid

        if search > midNum:
            low = mid + 1
        elif search < midNum:
            high = mid - 1
        
    return None 


testArr = [1,3,6,8,93,120,900,1000, 5555,6000]

print(binary_search(testArr, 6000))
        


