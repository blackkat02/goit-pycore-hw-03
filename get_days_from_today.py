import datetime


def get_days_from_today(date_str):
    """
    Calculate the number of days between the given date and today's date.
    Args:
        date_str (str): The date string in 'YYYY-MM-DD' format.
    Returns:
        int: The number of days between the given date and today's date.
    Raises:
        ValueError: If the date string is not in the correct format ('YYYY-MM-DD').
    """
    try:
        date_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please provide a date in 'YYYY-MM-DD' format. ")

    today = datetime.datetime.today().date()
    days_delta = today - date_date

    return days_delta.days


print(get_days_from_today('1943-12-06'))

