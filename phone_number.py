import re


def phone_number(list_numbers: str) -> str:
    """
    Normalizes a phone number to a standard format.

    Args:
        list_numbers: str: The phone number in any format.

    Returns:
        str: The normalized phone number in standard format (+38XXXXXXXXX).

    """
    pattern = r"[\D+]"
    modified_number = re.sub(pattern, "", list_numbers)
    print(modified_number)

    if not modified_number.startswith("+38"):
        modified_number = "+38" + modified_number

    return modified_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [phone_number(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
