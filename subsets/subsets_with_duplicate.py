class Solution:
    
    def subsetsWithDup(self, S):
        result = list()
        
        # boundary check
        if S is None or len(S) == 0:
            return result
        
        S = sorted(S)
        return self.subset_helper(result, list(), S, 0)
    
    def subset_helper(self, result, tmp_arr, S, index):
        result.append(tmp_arr[:])
        
        for i in xrange(index, len(S)):
            if i != index and S[i] == S[i-1]:
                continue
            
            tmp_arr.append(S[i])
            self.subset_helper(result, tmp_arr, S, i + 1)
            tmp_arr.pop(-1)
            
        return result

