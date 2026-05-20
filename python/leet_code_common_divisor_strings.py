class Solution:
    def menor_padrao(s: str) -> str:
        n = len(s)
        for tamanho in range(1, n + 1):
            padrao = s[:tamanho]
            # Verifica se s é prefixo de (padrao repetido)
            if all(s[i] == padrao[i % tamanho] for i in range(n)):
                return padrao
        return s

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size1 = len(str1)
        size2 = len(str2)
        
        subString = Solution.menor_padrao(str2)
        print(subString)
        if(all(str1[i] == str2[i % len(str2)] for i in range(len(str1)))):
            return subString
        return ""
        
