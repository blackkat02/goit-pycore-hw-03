import random


def get_numbers_ticket(start: int, end: int, quantity: int) -> list[int]:
    """
    Function generates a set of unique random numbers for such lotteries.
    Args:
        start (int): The minimum lottery number.
        end  (int): The maximum lottery number
        quantity  (int): The number of winning numbers.
    Returns:
        list[int]: The nlist of winning numbers.
    Raises:
        ValueError: If start, end, or quantity are not valid integers,
        or start is greater than end, or quantity is greater than the range of numbers.
    """
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(quantity, int):
        raise ValueError("Please enter valid integers for start, end, quantity.")

    if start > end:
        raise ValueError("Start cannot be greater than end.")

    if quantity > (end - start + 1):
        raise ValueError("Quantity cannot be greater than the number of possible unique numbers.")

    lottery_list = range(start, end + 1)
    lottery_win_numbers = random.sample(lottery_list, quantity)
    lottery_win_numbers.sort()
    return lottery_win_numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Виграшна комбінація:", lottery_numbers)
