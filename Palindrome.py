class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        temp = [int(k) for k in str(x)]
        result = None
        if len(temp) == 1:
            return True
        for n in range(int(len(temp))):
            if temp[n] == temp[len(temp) - 1 - n]:
                result = True
            else:
                result = False
                break
        
        return result