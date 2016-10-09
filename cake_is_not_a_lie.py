def answer(s):
    # your code here
    
    max_num_slices = 1
    
    for i in range(2,201):
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
        
        print(i)
        print(subsequences)
        print(sorted_subsequences)

        not_equal = False
        
        for j in range(0, len(subsequences)-1):
            if subsequences[j] != subsequences[j+1]:
                not_equal = True
        
        if not not_equal:
            max_num_slices = i
    
    return max_num_slices


print answer('bcabcabca')