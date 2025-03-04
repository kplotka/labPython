def round_numbers(numbers: list[int], treshold: int) -> list[int]:
    return [num // 10 * 10 if num < treshold else (num + 9) // 10 * 10 for num in numbers]