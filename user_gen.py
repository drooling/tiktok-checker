import itertools
import string

CHARS = int(input("How many characters? "))

with open("usernames.txt", 'w') as of:
    of.writelines({'\n'.join({''.join(combo) for combo in itertools.combinations_with_replacement(str(string.ascii_lowercase + string.digits), r=CHARS)})})
