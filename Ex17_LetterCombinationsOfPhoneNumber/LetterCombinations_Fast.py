
def letterCombinations(digits: str):

    # By using recursive method, decompose the 'digits' into digits.
    # Then each time get the first digit, then find it's dic-letters.
    # After that, recusivly find the after combinations.

    if digits == '':
        return ''

    dic = {}
    dic['2'] = {'a', 'b', 'c'} # faster
    dic['3'] = {'d', 'e', 'f'}
    dic['4'] = {'g', 'h', 'i'}
    dic['5'] = {'j', 'k', 'l'}
    dic['6'] = {'m', 'n', 'o'}
    dic['7'] = {'p', 'q', 'r', 's'}
    dic['8'] = {'t', 'u', 'v'}
    dic['9'] = {'w', 'x', 'y', 'z'}

    if len(digits) == 1:
        return dic[digits]

    letters = []
    for let in dic[digits[0]]:
        aft = letterCombinations(digits[1:])
        for af_let in aft:
            letters.append(let + af_let)

    return letters


print(letterCombinations('234'))
