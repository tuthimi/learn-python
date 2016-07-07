__author__ = 'Administrator'
import zipfile
from threading import Thread


def extractfile(zFile, password):
    try:
        print(password)
        zFile.extractall(pwd = password)
        print(password)
    except Exception, e:
        print (e)


def main():
    zFile = zipfile.ZipFile('evil.zip', 'r')
    pFile = open('dictionary.txt')
    for line in pFile.readlines():
        #extractfile(zFile, line.strip('\n'))
        t = Thread(target=extractfile, args=(zFile, line.strip('\n')))
        t.start()
    print('finished!')


if __name__ == '__main__':
    main()
