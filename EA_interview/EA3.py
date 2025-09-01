from typing import List


def compress(grid: List[str]) -> str:
    if not grid:
        return ""

    # Properly flatten grid considering row connections
    flat_str = "".join(grid)

    # Run-length encoding
    result = []
    current_char = flat_str[0]
    count = 1

    for char in flat_str[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count if count > 1 else ''}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count if count > 1 else ''}{current_char}")

    return "".join(result)

print(compress(["AAB", "BCC"]))