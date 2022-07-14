class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)
        n = n[2:]           # get rid of '0b'
        length = len(n)
        n = (32-length)*'0' + n     # make sure 32 bits
        #print(n)
        n = n[::-1]
        
        value = 0
        for i in range(0,length,8):
            value += int(n[i:i+8],2) * 256**(3-i//8)
        return value
