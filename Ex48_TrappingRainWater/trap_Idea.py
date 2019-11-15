
def trap(height) -> int:

    # the idea here is about using two way scanning and the overlapping
    # area would be the real area that contain water. First we scan from
    # the left, we assume that the right hand side would always higher
    # then the left hand side. Thus, the volume of all traps would only
    # be determined by the left hand side's height. (e.g we got [5,2]
    # then we would get volume (5-2=3). Again, we do this from right end,
    # (e.g we got [2,5] then we get volume(2-5 -> 2)). Then the minimum
    # one is the real volume we get, which can be represented by:
    # vol[i] = min(left_max - h[i], right_max - h[i])


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
