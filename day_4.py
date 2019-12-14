def criteria_checker(num, part_2=False):
    import re

    if len(num) != 6:
        return False

    current = 0

    for digit in num:
        if int(digit) < current:
            return False
        current = int(digit)

    if part_2:
        has_repeating = any(
            len(match.group()) == 2 for match in re.finditer(r"(\d)\1+", num)
        )
    else:
        has_repeating = any(re.finditer(r"(\d)\1+", num))

    return has_repeating


def main():
    puzzle_input = (278384, 824795)
    print("Part 1\n------")
    print("Test case (expected True): 111111 is {}".format(criteria_checker("111111")))
    print("Test case (expected False): 223450 is {}".format(criteria_checker("223450")))
    print("Test case (expected False): 123789 is {}".format(criteria_checker("123789")))

    print(
        "Answer for part 1: {}\n".format(
            sum(
                criteria_checker(str(num))
                for num in range(puzzle_input[0], puzzle_input[1] + 1)
            )
        )
    )

    print("Part 2\n------")
    print(
        "Test case (expected True): 112233 is {}".format(
            criteria_checker("112233", part_2=True)
        )
    )
    print(
        "Test case (expected False): 123444 is {}".format(
            criteria_checker("123444", part_2=True)
        )
    )
    print(
        "Test case (expected True): 111122 is {}".format(
            criteria_checker("111122", part_2=True)
        )
    )
    print(
        "Answer for part 2: {}\n".format(
            sum(
                criteria_checker(str(num), part_2=True)
                for num in range(puzzle_input[0], puzzle_input[1] + 1)
            )
        )
    )


if __name__ == "__main__":
    main()
