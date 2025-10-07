import re

def normalize_phone(phone_number):
    """
    Normalize a phone number to international format with +380 country code.
    
    This function cleans and standardizes Ukrainian phone numbers by removing
    non-digit characters (except leading +), and ensuring the result starts
    with the +380 country code.
    
    Args:
        phone_number (str): The phone number to normalize. Can contain spaces,
                           hyphens, parentheses, and other formatting characters.
                           Examples: "050 123 45 67", "+38(050)123-45-67",
                           "380501234567", "0501234567"
    
    Returns:
        str: Normalized phone number in format +380XXXXXXXXX where X are digits.
             Returns TypeError object if input is not a string (note: this is
             likely a bug, should raise instead of return).
    
    Normalization rules:
        - Removes all non-digit characters except + at the start
        - If starts with '+': keeps as is
        - If starts with '380': adds '+' prefix
        - If starts with '0': replaces '0' with '+380'
        - Otherwise: adds '+380' prefix
    
    Examples:
        >>> normalize_phone("    +38(050)123-32-34")
        '+380501233234'
        
        >>> normalize_phone("0503451234")
        '+380503451234'
        
        >>> normalize_phone("(050)8889900")
        '+380508889900'
        
        >>> normalize_phone("38050-111-22-22")
        '+380501112222'
        
        >>> normalize_phone("501234567")
        '+380501234567'
    
    Note:
        The function currently returns a TypeError object instead of raising
        it when the input is not a string. This should likely be changed to
        'raise TypeError(...)' instead of 'return TypeError(...)'.
    """
    
    if not isinstance(phone_number, str):
        return TypeError("phone number must be string")

    phone_number = re.sub(r'(?!^\+)\D', '', phone_number)

    if phone_number.startswith('+'):
        return phone_number
    elif phone_number.startswith('380'):
        return '+' + phone_number
    elif phone_number.startswith('0'):
        return '+380' + phone_number[1:]
    else:
        return '+380' + phone_number

for test in ["067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "38050123+4567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+48087654321",
    2]:
    try:
        print(normalize_phone(test))
    except Exception as e:
        print(e)
