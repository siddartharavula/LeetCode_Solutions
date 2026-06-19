class Solution(object):
    def isValid(self, s):
      if s[0] in ")}]" or s[-1] in "({[":
        return False
      ans=[]
      for i in range(len(s)):
        if s[i] in "({[":
          ans.append(s[i])
        elif s[i] in ")}]":
          if s[i]==')':
            p='('
          if s[i]=='}':
            p='{'
          if s[i]==']':
            p='['
          if ans==[] or p!=ans[-1]:
            return False
          else:
            ans.pop()
      if ans==[]:
        return True
      return False
      
      

      """
        :type s: str
        :rtype: bool
        """
        