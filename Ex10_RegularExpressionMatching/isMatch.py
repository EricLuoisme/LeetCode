
def isMatch(s: str, p: str) -> bool:
    # use DP, table to store results

    # T = [[False] * (len(p) + 1)] * (len(s) + 1) can not use this.
    T = [[False]*(len(p) + 1) for i in range(len(s) + 1)] # must use this
    T[0][0] = True # empty string matchs emty pattern

    for j in range(1, len(T[0])):
        if p[j - 1] == '*':
            T[0][j] = T[0][j - 2] # e.g. b match pattern a*b

    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            # if this char is exactly equal to the pattern, or pattern is '.'
            # then it should continue be Ture if left substring is True already.
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                T[i][j] = T[i - 1][j - 1]
                a = 0

            # if current pattern is '*', we have two situations
            elif p[j - 1] == '*':
                # e.g. b should match b*, or never used it
                T[i][j] = T[i][j - 2] # * used at least once
                if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                    # * never used, but the char before this repeatable char in
                    # the pattern matches current char in string
                    T[i][j] = T[i][j] or T[i - 1][j]
            else:
                T[i][j] = False # we must assign false over here

    return T[- 1][- 1]


s = 'a'
p = 'a*'
print(isMatch(s, p))
