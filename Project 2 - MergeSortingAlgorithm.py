def mergeLeftRight(arr):
  if len(arr) <= 1:
    return arr
  middle = len(arr) // 2
  left = arr[:middle]
  right = arr[middle:]
  sleft = mergeLeftRight(left)
  sright = mergeLeftRight(right)
  return mergeSort(sleft, sright)
 
def mergeSort(left, right):
  result = []
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result
  
arr = [16,21,11,8,12,22]
x = mergeLeftRight(arr)
print ("Solution array is:", x, "Time Complexity is O(nlogn)")