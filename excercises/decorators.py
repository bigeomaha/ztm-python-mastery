# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs) if args[0]['valid'] else None
  return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
