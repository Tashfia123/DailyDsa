class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

sol = Solution ()        
print(sol.isAnagram("rat","car"))
print(sol.isAnagram("bat","bata"))