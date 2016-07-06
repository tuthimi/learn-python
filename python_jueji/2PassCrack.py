__author__ = 'Administrator'
import crypt

def checkpass(userhash):
    salt = userhash[0:2]
    fdict = open('dictionary.txt', 'r')
    for line in fdict.readlines():
        if crypt.crypt(line, salt) == userhash:
            print ('The password' + line + 'right')


def main():
    fpass = open('passwords.txt', 'r')
    for line in fpass.readlines():
        username = line.split(':')[0]
        userhash = line.split(':')[1]
        checkpass(userhash)

if __name__ == '__main__':
    main()