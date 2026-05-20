# iterate only one
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxLenght: int = len(word2) if len(word1) < len(word2) else len(word1)
        
        mergedWord: list[str] = []
        for i in range(0,maxLenght):
            if i < len(word1):
                mergedWord.append(word1[i])
            if i < len(word2):
                mergedWord.append(word2[i])
        return "".join(mergedWord)

# Loop only while both strings still have characters, then append the leftover tail in one shot:
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        min_len = min(n1, n2)
        
        merged = []
        append = merged.append  # local binding avoids attribute lookup
        for i in range(min_len):
            append(word1[i])
            append(word2[i])
        
        # Append the remaining tail of whichever string is longer
        if n1 > n2:
            merged.append(word1[min_len:])
        elif n2 > n1:
            merged.append(word2[min_len:])
        
        return "".join(merged)
