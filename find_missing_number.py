def find_missing_number(numbers):
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

example = [3, 0, 1]
print("Missing number is:", find_missing_number(example))
def first_non_repeating_char(s):,
