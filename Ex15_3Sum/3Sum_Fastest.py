
import collections


def threeSum(nums):

    result = []
    d = collections.defaultdict(int) # by using this dictionary
                                    # even we do not meet 0 in nums
                                    # we check d[0], we can still get
                                    # an '0' as return and no error occur
    pos = set()
    neg = set()
    for num in nums: # seperate positive and negative numbers
        d[num] += 1
        if num > 0:
            pos.add(num)
        elif num < 0:
            neg.add(num)

    if d[0] >= 3:
        result.append([0,0,0])

    for p in pos:
        for n in neg:
            s = - p - n
            if s not in d:
                continue
            if s == 0 and d[0] > 0: result.append([n, 0, p])
            elif s == p and d[s] > 1: result.append([n, p, p])
            elif s == n and d[s] > 1: result.append([n, n, p])
            elif s > p and d[s] > 0: result.append([n, p, s])
            elif s < n and d[s] > 0: result.append([s, n, p])

    return result



s = [-1, 0, 1, 2, -1, 4]
print(threeSum(s))
