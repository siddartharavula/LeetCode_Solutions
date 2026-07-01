class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        s=s.lower()
        for x in s:
            if x.isalpha() or x in "0987654321":
                ans+=x
        return ans==ans[::-1]
        