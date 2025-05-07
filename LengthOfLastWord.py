class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return len(s.strip().split()[-1])
        word = s.strip()
        splitted = s.split()
        finalword = splitted[-1] 
        length = len(finalword)
        return length