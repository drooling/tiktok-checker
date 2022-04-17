import argparse
import itertools
import string


def characters():
    with open("usernames.txt", 'w') as of:
        of.writelines({'\n'.join({''.join(combo) for combo in itertools.combinations_with_replacement(str(
            string.ascii_lowercase + string.digits), r=CHARS) if not ''.join(combo).isnumeric() and any(chr.isdigit() for chr in ''.join(combo))})})
        of.close()


def letters():
    with open("usernames.txt", 'w') as of:
        of.writelines({'\n'.join({''.join(combo) for combo in itertools.combinations_with_replacement(
            str(string.ascii_lowercase), r=CHARS)})})
        of.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', action='store_true',
                        dest='letters', required=False)
    args = parser.parse_args()
    CHARS = int(input("How many characters? "))
    if args.letters:
        letters()
    else:
        characters()
