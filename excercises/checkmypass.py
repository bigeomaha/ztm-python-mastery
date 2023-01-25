import sys
import requests
import hashlib

def get_pwned_passwords(shapass):
    pass_check_url = 'https://api.pwnedpasswords.com/range/' + shapass[:5]
    res = requests.get(pass_check_url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code} returned.')
    return res.text

def is_pass_pwned(shapass, responses):
    passwords = ( line.split(':') for line in responses.split('\r\n'))
    for hashed, hash_count in passwords:
        if shapass[5:] == hashed:
            return f'Your pass has been pwned {hash_count} times!\n\n'

    return f'Great choice, you have not been pawned.\n\n'


def hash_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def request_password():
    supplied_pass = input('What password would you like to check?\t')
    return supplied_pass
def restart():
    ans = input('Would you like to test another one? (t/f)\t')
    if ans.lower() == 't':
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        check_password = request_password()
        hashed_password = hash_password(check_password)
        pwnd_list = get_pwned_passwords(hashed_password)
        is_pwned = is_pass_pwned(hashed_password, pwnd_list)
        print(is_pwned)
        if not restart():
            break
