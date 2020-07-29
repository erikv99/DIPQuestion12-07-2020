# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

class Solution: 

  def getRange(self, arr, target):
    
      # Adding all the indexes of elements of the array that are equal to our target to a new array
      indices = [i for i, currentNum in enumerate(arr) if currentNum == target]
      
      # If there is 1 or 0 indices found (num is only present once, or not at all)
      if (len(indices) < 2):

          return [-1]

      # Getting the first and last index and returning the result
      result = [indices[0], indices[len(indices) - 1]]
      return result

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
target = 9

sol = Solution().getRange(arr, target)
print(sol)
# [1, 4]