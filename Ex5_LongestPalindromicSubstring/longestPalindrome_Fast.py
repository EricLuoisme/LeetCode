
def longestPalindrome(s):
    # Using the Manacher's algorithm

    T = '#'.join('${}@'.format(s)) # rebuild the string to facilitate the algorithm
    p_len = [0] * len(T) # store the length of palindrome on it's centre at i
    centre = 0 # current centre pointer
    r_boundary = 0 # current right boundary pointer

    print(T)

    for i in range(len(T) - 1):
        # because the last one char (@), we don't even need to check it

        mirror = 2 * centre - i # get the mirror centre of this i

        if i < r_boundary: # if i is within the right boundary, we could use
                            # rules.
            p_len[i] = min(r_boundary - i, p_len[mirror])
            # here we use the rules we observed. If a palindrome with this centre i,
            # can be extend beyond the right boundary, plen[i] should be equal or
            # greater than plen[mirror]. If it can be extended beyond the left boundary
            # then plen[i] should be equal or greater then right boundary's index -
            # i's index

        while T[(i - p_len[i]) - 1] == T[(i + p_len[i]) + 1]:
            p_len[i] += 1
            # here is about, try to extend the palindrome with i as it's centre
            # (i - p_len[i]) means: we already know centre at i, would result a
            # palindrome with length p_len[i] in s. But in T, we have 'bars' between
            # two chars, then in T, a palindrome with length L in s would result
            # in length 2 * L in T. Thus, we can 'cut' the part that we already know
            # it would be a palindrome (from i - p_len[i] to i + p_len[i]). Then we
            # start from comparing (i - p_len[i]) - 1 and (i + p_len[i]) + 1.

        if i + p_len[i] > r_boundary:
            # if current centre's palindrome is longer than the last one, which
            # also means that right half of this palindrome is greater than right
            # half of last palindrome, we should replace a new centre and new
            # right boundary
            centre = i
            r_boundary = i + p_len[i]

    real_centre = p_len.index(max(p_len))
    longestP = T[real_centre - p_len[real_centre] : \
                            real_centre + p_len[real_centre]] # cut the palindrome
    longestP = longestP.replace('#', '')
    longestP = longestP.replace('@', '')
    longestP = longestP.replace('$', '')
    return longestP


print(longestPalindrome("babad"))
