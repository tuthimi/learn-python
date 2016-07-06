__author__ = 'Administrator'


def checkpass(userhash):
    salt = userhash[0:2]
    fdict = open('dictionary.txt', 'r')
    for line in fdict.readlines():
        if line.strip('\n') == userhash:
            print ('The password: ' + line.strip('\n') + ' is right ')
            return True
    return False

def main():
    fpass = open('passwords.txt', 'r')
    for line in fpass.readlines():
        username = line.split(':')[0]
        userhash = line.split(':')[1]
        if checkpass(userhash.strip(' ')):
            print('to user '+ username)

if __name__ == '__main__':
    main()