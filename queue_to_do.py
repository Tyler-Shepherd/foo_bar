#Gets the xor sum of all numbers up to a
def get_xor_up_to(a):
     result = [a,1,a+1,0]

     return result[a%4]


def answer(start, length):
    
    checksum = get_xor_up_to(start-1);

    for row in range(1, length-1):

        checksum = checksum ^ get_xor_up_to(start + row*length + length - 1)
        checksum = checksum ^ get_xor_up_to(start + row*length + length - row - 1)
        
    checksum = checksum ^ get_xor_up_to(start + length*(length-1))  

    return checksum

print answer(0,3)