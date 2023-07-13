class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0
        intr = 0
        cntT = 0
        cntF = 0
        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                cntT += 1
            else:
                cntF += 1
            while cntF > k and cntT > k:
                if answerKey[intr] == 'F':
                    cntF -= 1
                else:
                    cntT -= 1
                intr += 1
            result = max(result , i - intr +1)
        return result