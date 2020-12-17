import sys
import time


def check_palindrome(palindrome_string):
    max_length = len(palindrome_string)
    print(f"This is the number of characters being read: {max_length}")
    index = 0
    while index < max_length/2:
        if palindrome_string[index] != palindrome_string[max_length - 1 - index]:
            return False
        index += 1
    return True


def main():
    timer = time.time()
    input_file = sys.argv[1]
    with open(input_file) as reader:
        potential_palindrome = reader.read()
    if check_palindrome(potential_palindrome):
        print("Yes this is a palindrome")
    else:
        print("No this isn't a palindrome")
    timer = time.time() - timer
    print(f"Execution took this long: {timer}")
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
