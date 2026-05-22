from typing import List

'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(len(flowerbed)==1):
            if(flowerbed[0]==0 and n==1):
                return true
            return false
        for i in range(1,len(flowerbed)-1):
            if(i==1 and (flowerbed[i-1]+flowerbed[i])==0):
                flowerbed[i-1]=1
                n = n -1
            if(i==len(flowerbed)-2 and (flowerbed[i]+flowerbed[i+1])==0):
                print(flowerbed)
                flowerbed[i+1]=1
                n = n -1
            sum = flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]
            if(sum == 0):
                flowerbed[i]=1
                n = n -1
        return n == 0

'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        
        # Padding com zeros nas pontas elimina os casos especiais de borda
        bed = [0] + flowerbed + [0]
        
        for i in range(1, len(bed) - 1):
            if bed[i-1] == 0 and bed[i] == 0 and bed[i+1] == 0:
                bed[i] = 1
                n -= 1
                if n == 0:m
                    return True
        
        return False