import random
import sys


def abort(msg):
    print('Exited with Err:')
    print("\t" + msg)
    exit(1)


rand_num = None


def get_random_number(s, e):
    global rand_num
    rand_num = random.randint(start_num, end_num)


def guess_number():
    while True:
        guess = input("What number am I thinking of? ")
        if guess == number:
            print('Great job, you guessed it!!')
            break
        else:
            print('Sorry, please try again.')


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        abort('Please provide start and end numbers.')

    try:
        # Ensure integers and positive numbers
        start_num = abs(int(sys.argv[1]))
        end_num = abs(int(sys.argv[2]))

    except ValueError:
        abort('Start and End must be integers')

    number = get_random_number(start_num, end_num)
    guess_number()
