class Container:

    def __init__(self): 
        self.intArr = []
        

    def add(self, value:int):
        self.intArr.append(value)

    def remove(self, value:int):
        try:
            self.intArr.remove(value)
            return True 
        except: 
            return False
        
    
    def get_median(self):
        if len(self.intArr) == 0:
            return None
        self.intArr = self.merge_sort(self.intArr)
        midNum = len(self.intArr)//2
        print(self.intArr) 
        print("Midnum", midNum)
        if len(self.intArr) % 2 == 0:
            #Even length array, meaning the medium is between two numbers mid & mid -1 
            return self.intArr[midNum - 1]
        else:
            #Odd length array 
            return self.intArr[midNum]
            

    def merge_sort(self, array):
        if len(array) == 1:
            return array
        
        mid = len(array)//2

        left = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])

        return self.merge(left, right)

    def print_container(self):
        print(self.intArr)

    def merge(self, left, right):

        i = 0
        j = 0 
        sorted_arr = []
        leftLen = len(left)
        rightLen = len(right)

        while i < leftLen and j < rightLen:
            leftNum = left[i]
            rightNum = right[j]

            if leftNum < rightNum:
                sorted_arr.append(leftNum)
                i += 1 
            else:
                sorted_arr.append(rightNum)
                j += 1 
        
        if i == leftLen:
            sorted_arr.extend(right[j:])
        else:
            sorted_arr.extend(left[i:])

        return sorted_arr

#[3,8,8,4,2,2]

#[3,8,8] [4,2,2]

#[3] [8,8] [4] [2,2]
   
        