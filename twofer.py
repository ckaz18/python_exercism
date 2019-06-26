import sys

def checkString(user):
    if (not user):
        print('One for you, one for me')
    else:
        print(f'One for {user}, one for me.')
        # need to figure out args

if __name__ == '__main__':
    checkString(sys.argv[1:])
