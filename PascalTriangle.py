class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Ptri = [[1]]
        for i in range(1,numRows):
            l = Ptri[i-1]
            ll = l+[0]
            lr = [0]+l
            #print(ll, lr)
            Ptri.append( [ll[j]+lr[j] for j in range(len(ll))] )
        return Ptri
