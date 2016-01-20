# http://www.lintcode.com/en/problem/k-closest-numbers-in-sorted-array/#

class Solution:
    
    def findCloestNumberIndex(self, A, target):
        if A is None or len(A) == 0:
            return None
        
        low = 0
        high = len(A) - 1
        
        while low + 1 < high:
            mid = low + (high - low) / 2
            
            if A[mid] == target:
                return mid
                
            elif A[mid] < target:
                low = mid
            
            else:
                high = mid
        
        if abs(A[low] - target) <= abs(A[high] - target):
            return low
            
        else:
            return high
    
    def kClosestNumbers(self, A, target, k):
        result = list()
        
        if A is None or len(A) == 0:
            return result
        
        for i in xrange(k):
            idx = self.findCloestNumberIndex(A, target)
            
            if idx is None:
                break
            
            result.append(A[idx])
            A.pop(idx)
        
        return result
