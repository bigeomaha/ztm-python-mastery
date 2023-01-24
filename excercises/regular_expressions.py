import re


def check_password(password):
    exp = re.compile(r"(^[a-zA-Z0-9@\$#%]{6,}\d\d$)")
    check = exp.match(password)
    if check is None:
        return False
    else:
        return True


if __name__ == "__main__":
    ipass = input("What is your password? ")

    if check_password(ipass):
        print('Great password!')
    else:
        print('you suck!')
