def first_non_repeating_char(s):
    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return None
     print("Input: 'Hello' -> Output:", first_non_repeating_char("Hello"))
      print("input: 'Swiss' -> Output :", first_non_repeating_char("Swiss"))
      