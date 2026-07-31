class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0:
                    if i + 1 == len(flowerbed) or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue 
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0:
                    if i == 0 or flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue     
                continue
            elif flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0