
def lengthOfLongestSubstring(s: str) -> int:
    # instead of using a list to keep tracking meeted characters,
    # we could make if faster by using a string to store

    if len(s) == 0:
        return 0

    meet_char = s[0]
    max_len = 1 # here we at least contain s[0], one single character
    
    for char in s[1:]:
        if char in meet_char:
            index = meet_char.find(char)
            meet_char = meet_char[index + 1:]
            # cut the meeted list to only contain part after repeated char
        meet_char += char # keep adding the char
        if len(meet_char) > max_len:
            max_len = len(meet_char)

    return max_len
