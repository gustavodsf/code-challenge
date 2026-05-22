
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: List[str] = ['a','A','e','E','i','I','o','O','U','u']
        existinVowels = []
        for c in s:
            if c in vowels:
                existinVowels.append(c)
        existinVowels.reverse()
        idx = 0
        newStr: List[str] = []
        for i in range(len(s)):
            temp = s[i]
            if(s[i] in vowels):
                temp = existinVowels[idx]
                idx+=1
            newStr.append(temp)
        return "".join(newStr)
'''
class Solution:
    _VOWELS = frozenset('aeiouAEIOU')

    def reverseVowels(self, s: str) -> str:
        vowels = self._VOWELS
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)