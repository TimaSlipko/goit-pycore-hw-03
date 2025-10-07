from datetime import datetime

def get_days_from_today(date):
    """
    Calculate the number of days from today to the specified date.
    
    Args:
        date (str): A date string in 'YYYY-MM-DD' format (ISO 8601).
    
    Returns:
        int: The number of days between today and the given date.
            Positive values indicate future dates, negative values indicate past dates.
    
    Raises:
        ValueError: If the date string is not in the correct 'YYYY-MM-DD' format
                    or represents an invalid date (e.g., '2025-13-45').
        TypeError: If the date argument is not a string.
    
    Examples:
        >>> get_days_from_today('2025-12-25')
        79
        >>> get_days_from_today('2025-01-01')
        -279
    """
    try:
        d = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        diff = d - today
        return diff.days
    except ValueError as e:
        raise ValueError("invalid date format") from e
    except TypeError as e:
        raise TypeError("invalid date type") from e

for test in ['2025-09-08', '2026-08-25', 'cc', 5]:
    try:
        print(get_days_from_today(test))
    except Exception as e:
        print(e)

