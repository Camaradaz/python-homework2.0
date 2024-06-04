# Given a flowerbed represented as a list 
# of 0s and 1s where

# 0 means empty
# 1 means not empty

# Determine if n flowers, can be placed
# such that flowers cannot be planted
# adjacent from each other

def can_place_flowers(flowerbed, n):
    if n == 0:
        return True
    
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            is_left_empty = i == 0 or (flowerbed[i - 1] == 0)
            is_right_empty = i == length - 1 or (flowerbed[i + 1] == 0)
            if is_left_empty and is_right_empty:
                flowerbed[i] = 1 
                count += 1
                if count == n:
                    return True
    
    return count >= n