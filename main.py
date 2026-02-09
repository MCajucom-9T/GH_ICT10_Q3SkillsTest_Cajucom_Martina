# if-elif-else statement in python
from pyscript import display, document


def account_authentication(e):
    document.getElementById('output').innerHTML = " "
    password = document.getElementById('input2').value # collecting value from an input field
    lengthpw = len(password)
    username = len(document.getElementById('input1').value)

    if not password.isalpha() and username > 6:
        if password.isalpha() and not password.isdigit():
            display(f'Your passsword has to contain numbers', target='output')
        elif not password.isalpha() and password.isdigit():
            display(f'Your password has to contain letters', target='output')
        else:
            display(f'Your password and username is valid', target='output')
    elif not username > 6 and not lengthpw > 9:
        display(f'Your username needs to have at least 7 characters and password needs to have at least 10 characters.', target='output')
    elif not username > 6 and lengthpw > 9:
        display(f'Your username needs to have at least 7 characters.', target='output')
    elif username > 6 and not lengthpw > 9:
        display(f'Your password needs to have at least 10 characters.', target='output')
    else:
        display(f'Your password MUST contain both letters and numbers.', target='output')
    