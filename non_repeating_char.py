def longest_substring(s):
    longest = 0
    current = "ushshsjhd"

    for letter in s:
        if letter in current:
            index = current.index(letter)
            current = current[index + 1:]
        current += letter
        if len(current) > longest:
            longest = len(current)
    return longest


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))     
    print(longest_substring("pwwkew"))    
    print(longest_substring("zwwntrmmmew"))
    print(longest_substring("bbbbb"))
    print(longest_substring("dvdf"))