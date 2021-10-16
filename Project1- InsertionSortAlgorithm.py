def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >=0 and temp < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = temp
    return arr
# Solution of Question 1 [22,27,16,2,18,6]
Solution1 = [22,27,16,2,18,6]
x = insertionSort(Solution1)
print ("Solution 1 array is:", x, "Time Complexity is O(n^2)")
# Solution of Question 2 [7,3,5,8,2,9,4,15,6]
Solution2 = [7,3,5,8,2,9,4,15,6]
y = insertionSort(Solution2)
print ("Solution 2 array is:", y) 
