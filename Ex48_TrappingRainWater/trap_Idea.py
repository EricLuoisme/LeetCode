
def trap(height) -> int:

    # from left to right
    left_max = 0
    right_max = 0
    left2right = []
    right2left = []
    i = 0
    j = len(height) - 1
    
    while i < len(height):
        if height[i] > left_max:
            left_max = height[i]
        left2right.append(left_max - height[i])

        if height[j] > right_max:
            right_max = height[j]
        right2left.append(right_max - height[j])

        i += 1
        j -= 1

    right2left = right2left[::-1] # reverse it

    all = []
    for i in range(len(height)):
        all.append(min(left2right[i], right2left[i]))

    return sum(all)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
