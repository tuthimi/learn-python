__author__ = 'Administrator'
import zipfile


def extractfile(zFile, password):
    try:
        zFile.extractall(pwd = password)
        print(password)
    except Exception, e:
        print (e)


def main():
    zFile = zipfile.ZipFile('evil.zip', 'r')
    pFile = open('dictionary.txt')
    for line in pFile.readlines():
        extractfile(zFile, line.strip('\n'))
    print('finished!')


if __name__ == '__main__':
    main()
