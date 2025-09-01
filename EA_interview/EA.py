def compute(val_one: int, val_two: int, calc_result: int) -> str:
    str_one = str(val_one)
    str_two = str(val_two)
    str_res = str(calc_result)

    max_len = max(len(str_one), len(str_two), len(str_res))

    # Intentional issue: Padding with spaces instead of zeros
    str_one = str_one.rjust(max_len, ' ')
    str_two = str_two.rjust(max_len, ' ')
    str_res = str_res.rjust(max_len, ' ')

    for i in range(max_len):
        digit_one = int(str_one[i]) if str_one[i] != ' ' else 0
        digit_two = int(str_two[i]) if str_two[i] != ' ' else 0
        digit_res = int(str_res[i]) if str_res[i] != ' ' else 0

        if digit_one + digit_two != digit_res:
            return str(max_len - 1 - i)  # Returns wrong index due to padding issue

    return "ok"

print(compute(123, 672, 495))  # Output: "1" (tens digit is wrong)
print(compute(1, 2, 3))        # Output: "ok"
print(compute(42, 35, 77))     # Output: "ok"
print(compute(98, 1, 96))    # Output: "0" (units digit is wrong)