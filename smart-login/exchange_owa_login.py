#coding=utf-8

import urllib,urllib2,cookielib,gzip,StringIO,re

def ungzip(data):
    try:
        print('unzipping...'),
        compressedstream = StringIO.StringIO(data)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        data = gzipper.read()
        print('done!')
    except:
        print('not zip!')
    return data



def searchkeyword(searchstr,username,password):
    cj=cookielib.CookieJar()
    opener  =urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    urllib2.install_opener(opener)

    login_url=r'https://mail.exchangeowa.com/CookieAuth.dll?Logon'

    # if password[-1] == '\n':
    #     password = password[:-1]

    headers = {"User-Agent": "Opera/9.80 (Windows NT 5.1; U; Edition IBIS; en) Presto/2.10.229 Version/11.64",
               "Host": "mail.exchangeowa.com",
                "Accept":"text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1",
                "Accept-Language":"en-US,en;q=0.9",
                "Accept-Encoding":"gzip, deflate",
                "Referer":"https://mail.exchangeowa.com/CookieAuth.dll?GetLogon?curl=Z2Fowa&reason=0&formdir=2",
                "Connection":"Keep-Alive",
                "Content-Length":"103",
                "Content-type":"application/x-www-form-urlencoded"}
    login_data=urllib.urlencode({'curl':'Z2Fowa',
                                 'flags':'0',
                                 'forcedownlevel':'0',
                                 'formdir':'2',
                                 'username':username,
                                 'password':password,
                                 'isUtf8':'1',
                                 'trusted':'0'})
    try:
        req=urllib2.Request(login_url,login_data,headers)
        content=opener.open(req)
        msg = ungzip(content.read())

        username = username.split('\\')[1]

        file_object = open(username+'_1.html', 'wb')
        file_object.write(msg)
        file_object.close()


        pattern = re.compile('a_sFldId = \"(.*)\"', flags = 0)
        userid = re.findall(pattern,msg)
        dec_userid = urllib.unquote(userid[0])

    except:
        print('[-]login failed!')
        return

    searchstr = urllib.urlencode({'ae':'Folder',
                                  't':'IPF.Note',
                                  'newSch':'1',
                                  'scp':'3',
                                  'id': dec_userid,
                                  'slUsng':'0',
                                  'sch': searchstr})
    searchurl = 'https://mail.exchangeowa.com/owa/?' + searchstr

    try:
        content2=opener.open(searchurl)
        msg2 = content2.read()

        if msg2.find('errMsg') > 0:
            pattern = re.compile('href = \"(.*)\"', flags = 0)
            errstr = re.findall(pattern,msg2)
            print errstr[3]


        file_object = open(username+'_2.html', 'wb')
        file_object.write(msg2)
        file_object.close()
        print('[+]search done!')

    except:
        print('[-]search wrong!')
        return



def main():
    searchstr = raw_input("the word to search:") 
    #raw_input 和 input： raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，
    #除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
    file = open('password.txt','r')
    done = 0
    while not done:
            aLine = file.readline()
            if(aLine != ''):
                username = aLine.split(' ')[0]
                username = username.strip()
                print(username)
                password = aLine.split(' ')[1]
                password = password.strip()
                print(password)
                searchkeyword(searchstr,username,password)
            else:
                done = 1
    file.close()

if __name__ == '__main__':
    main()