"""
Question:
Write a function that validates whether a given string is alphanumeric.

Conditions:
- The string must contain at least one character.
- Only uppercase letters (A-Z), lowercase letters (a-z), and digits (0-9) are allowed.
- No spaces, underscores (_), or special characters are allowed.

Return:
- True if the string is alphanumeric.
- False otherwise.
"""


def alphanumeric(password: str) -> bool:
    
    if password:

        for i in password:
            if not 97 <= ord(i) <= 122 and not 65 <= ord(i) <= 90 and not 48 <= ord(i) <= 57:
                return False

        return True
    
    return False

tests = [
    ("hello world_", False),
    ("PassW0rd", True),
    ("     ", False)
]
for s, b in tests:
    print(alphanumeric(s), b)


