from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
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
