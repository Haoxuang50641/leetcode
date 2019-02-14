class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        result = 0
        Jlist = list(J)
        Slist = list(S)
        for n in range(len(Jlist)):
            for m in range(len(Slist)):
                if Jlist[n] == Slist[m]:
                    result += 1
        
        return result