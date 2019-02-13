class Solution:
    def reverse(self, x: 'int') -> 'int':
        temp = []
        answer = 0
        answer2 = 0
        if x < 0:
            temp = list(reversed(str(-x)))
            answer = [str(sub) for sub in temp]
            answer2 = int("".join(answer))
            answer2 = answer2 * -1
        else:
            temp = list(reversed(str(x)))
            answer = [str(sub) for sub in temp]
            answer2 = int("".join(answer))
        
        if answer2 > 2147483648 or answer2 < -2147483648:
            return 0
        else:
            return answer2