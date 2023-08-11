def maxArea(height):
    l =0
    r = len(height) -1
    res = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        elif height[r] < height[l]:
            r -= 1
        else:
            return res 
        

print(maxArea([1,8,6,2,5,4,8,3,7]))
