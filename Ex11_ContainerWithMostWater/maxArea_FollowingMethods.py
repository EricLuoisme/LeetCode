
def maxArea(height) -> int:
    # the method here is about using the two finxed boundaries:
    # the left and the right boundaries, we can first start with these two
    # and narrow them.

    l_p = 0
    r_p = len(height) - 1
    volume = (r_p - l_p) * min(height[l_p], height[r_p]) # get an initialisation

    while l_p < r_p: # while we try all possible situations, untill overlap
        if height[l_p] > height[r_p]:
            # here is the crucial stuff, if left pointer's height is higher then
            # the right pointer's one. Then thinking by counter example, if we move
            # the left pointer (higer one), to right, then we might get a higher
            # one or a lower one. Because the distance between left and right pointer
            # is narrowed, if we got a lower one, we must results in a smaller
            # volume. If we a get a higher one, we still results in a smaller
            # volume. Why? Because the 'real' using height is min(h_left, h_right)
            # even we get a higher left pointer, we would still using the right
            # one to calculate the volume. Thus, we should move the right pointer
            # to the left
            r_p -= 1
        else:
            l_p += 1
        volume = max(volume, (r_p - l_p) * min(height[l_p], height[r_p]))
    return volume


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(maxArea(height))
