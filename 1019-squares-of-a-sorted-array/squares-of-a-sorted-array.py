class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        neg = []
        pos = []

        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        if len(neg) == 0:
            return [x*x for x in pos]

        elif len(pos) == 0:
            return [x*x for x in neg][ : :-1]

        else:
            pos = [x*x for x in pos]
            neg = [x*x for x in neg][ : : -1]
            res = []
            n = len(neg)
            m = len(pos)
            i=0
            j=0

            while (i<n) and (j<m):
                if neg[i] <= pos[j]:
                    res.append(neg[i])
                    i+=1

                else:
                    res.append(pos[j])
                    j+=1

            while i<n:
                res.append(neg[i])
                i+=1

            while j<m:
                res.append(pos[j])
                j+=1

        return res
