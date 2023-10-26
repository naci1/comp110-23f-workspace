def sum_evens_of_list(input_list: list[int]) -> int:
    """Loop over a list and sum all even elements"""
    sum_total: int = 0
    for i in range(len(input_list)):
        if i % 2 == 0:
            sum_total += input_list[i]
    return sum_total