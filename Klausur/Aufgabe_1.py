def check_password(password):
    specialChar = False
    letter = False
    digit = False
    passwordOK = False

    if len(password) >= 10:
        i = 0

        while i < len(password):
            zeichen = password[i]

            if zeichen.isdigit():
                digit = True
            else:
                if zeichen.isalpha():
                    letter = True
                else:
                    specialChar = True

            i = i + 1

        if letter and digit and specialChar:
            passwordOK = True

    return passwordOK

print(check_password("abc123$xyz"))   # True
print(check_password("abcdefghij"))   # False
print(check_password("1234567890"))   # False
print(check_password("!!!!!!!!!!"))   # False
print(check_password("abc1234567"))   # False
print(check_password("abcde$fghi"))   # False
print(check_password("ab1$"))         # False
print(check_password("12345abc$%"))   # True