class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha2 = []
        alpha = []
        for i in s:
            if i.isalnum() == True:
                alpha.append(i)
                alpha2.append(i)
        alpha2.reverse()
        if alpha == alpha2:
            return(True)
        else:
            return(False)