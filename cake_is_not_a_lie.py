# Problem: Find the maximum number of equal subsequences a string can be broken into

# Runtime complexity: O(logn), as it only has to operate for factors of n,
#   as it is not possible for subsequences to match when they are of different lengths

# Space complexity: O(n)

def answer(s):
    
    for i in range(len(s),2,-1):
        # i = number of slices
        
        if len(s)%i != 0:
            continue
        
        subsequences = []
        
        length_of_subsequence = len(s)/i;
        
        for j in range(0,i):
            start_pos = j*length_of_subsequence
            subsequences.append(s[start_pos:start_pos+length_of_subsequence])
            
        sorted_subsequences = []    
            
        for subsequence in subsequences:
            sorted_subsequences.append(sorted(subsequence))

        all_equal = True
        
        for j in range(0, len(subsequences)-1):
            if sorted_subsequences[j] != sorted_subsequences[j+1]:
                all_equal = False
                break
        
        if all_equal:
            return i
    
    return 1

# Test case
#print answer('acbabcabcabc')