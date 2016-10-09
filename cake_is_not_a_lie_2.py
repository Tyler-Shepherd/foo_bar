def answer(s):
    # your code here
    
    for i in range(len(s),2,-1):
        # i = number of slices

        print(i)
        
        #if i > len(s):
        #    break
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
        print(sorted_subsequences)


        all_equal = True
        
        for j in range(0, len(subsequences)-1):
            if sorted_subsequences[j] != sorted_subsequences[j+1]:
                all_equal = False
                break
        
        if all_equal:
            return i
    
    return 1

print answer('acbabcabcabc')