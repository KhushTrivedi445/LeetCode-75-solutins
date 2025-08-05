# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        vowels="aeiouAEIOU"
        l=list(s)
        i=0
        j=len(l)-1
        while i<j:
            if l[i]  not in vowels:
                i+=1
            elif l[j]  not in vowels:
                j-=1
            else:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
        return "".join(l)
                
        




s=Solution()
s1="icecream"
print(s.reverseVowels(s1))