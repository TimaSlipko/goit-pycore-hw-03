from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
    """
    Get a list of users with birthdays in the next 7 days, adjusted for weekends.
    
    This function identifies users whose birthdays fall within the next 7 days
    and returns their congratulation dates. If a birthday falls on a weekend
    (Saturday or Sunday), the congratulation date is moved to the following Monday.
    
    Args:
        users (list): A list of dictionaries, where each dictionary contains:
            - 'name' (str): The user's name
            - 'birthday' (str): The user's birthday in 'YYYY.MM.DD' format
    
    Returns:
        list: A list of dictionaries containing users with upcoming birthdays.
              Each dictionary has:
            - 'name' (str): The user's name
            - 'birthday' (str): The congratulation date in 'YYYY.MM.DD' format
                               (adjusted to Monday if the birthday falls on a weekend)
    
    Raises:
        TypeError: If users is not a list
        ValueError: If any user dictionary is missing required fields, has invalid
                   data types, or contains an invalid date format
    
    Example:
        >>> users = [
        ...     {"name": "John Doe", "birthday": "1985.10.10"},
        ...     {"name": "Jane Smith", "birthday": "1990.10.15"}
        ... ]
        >>> get_upcoming_birthdays(users)
        [{'name': 'John Doe', 'birthday': '2025.10.10'}]
    
    Note:
        - The function considers birthdays within the next 7 days from today
        - Weekend birthdays (Sat=5, Sun=6) are shifted to the following Monday
        - The year in the input birthday is replaced with the current or next year
    """
    if not isinstance(users, list):
        raise TypeError("users must be a list")
    
    if not all(
        isinstance(user, dict) and
        'name' in user and
        'birthday' in user and
        isinstance(user['name'], str) and
        isinstance(user['birthday'], str)
        for user in users
    ):
        raise ValueError("invalid data")
    
    birthdays = []
    
    for user in users:
        try:
            d = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError as e:
            raise ValueError("invalid date format") from e
        
        today = datetime.today().date()
        next_birthday = d.replace(year=today.year)

        if next_birthday < today:
            next_birthday = next_birthday.replace(year=next_birthday.year+1)

        if (next_birthday-today).days <= 7:
            if next_birthday.weekday() == 5:
                next_birthday += timedelta(days=2)
            elif  next_birthday.weekday() == 6:
                next_birthday += timedelta(days=1)
            
            birthdays.append({"name": user["name"], "birthday": next_birthday.strftime('%Y.%m.%d')})

    return birthdays


tests = [
    [
        {"name": "Jisoo", "birthday": "1985.10.10"},
        {"name": "Lisa", "birthday": "1990.01.27"},
        {"name": "Rose", "birthday": "1990.05.14"},
        {"name": "Jennie", "birthday": "1990.02.27"},
        {"name": "Yeji", "birthday": "1990.09.27"},
        {"name": "Ryujin", "birthday": "1991.10.07"},
        {"name": "Lia", "birthday": "1990.10.08"},
        {"name": "Yuna", "birthday": "1990.10.11"},
    ],
    2,
    [
        {"name": "Jisoo"},
    ],
    [
        {"name": 3, "birthday": "1990.10.11"},
    ]
]

for test in tests:
    try:
        print(get_upcoming_birthdays(test))
    except Exception as e:
        print(e)
