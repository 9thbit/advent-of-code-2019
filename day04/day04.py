
def check_digits(digits):
    # Check two adjacent digits are the same
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            break
    else:
        return False

    # Check non-decreasing
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False

    return True


def check_larger_group_matching(digits):
    last_digit, match_count = None, None
    for digit in digits + [None]:
        if digit == last_digit:
            match_count += 1

        else:
            if match_count == 2:
                return True
            match_count = 1
            last_digit = digit

    return False


def main():
    lower_bound, upper_bound = 156218, 652527
    part1_count = part2_count = 0
    for x in range(lower_bound, upper_bound + 1):
        digits = list(map(int, str(x)))
        part1_satisfied = check_digits(digits)
        part1_count += part1_satisfied

        if part1_satisfied and check_larger_group_matching(digits):
            part2_count += 1

    print(f'Part 1: {part1_count}')
    print(f'Part 2: {part2_count}')


if __name__ == "__main__":
    main()
