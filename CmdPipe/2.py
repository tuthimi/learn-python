#!python2
#coding:utf-8

# sys.stdout重定向
import os, sys, cStringIO
class RedirectStdout: #import os, sys, cStringIO
    def __init__(self):
        self.content = ''
        self.savedStdout = sys.stdout
        self.memObj, self.fileObj, self.nulObj = None, None, None

    #外部的print语句将执行本write()方法，并由当前sys.stdout输出
    def write(self, outStr):
        #self.content.append(outStr)
        self.content += outStr

    def toCons(self): #标准输出重定向至控制台
        sys.stdout = self.savedStdout #sys.__stdout__

    def toMemo(self): #标准输出重定向至内存
        self.memObj = cStringIO.StringIO()
        sys.stdout = self.memObj

    def toFile(self, file='out.txt'): #标准输出重定向至文件
        self.fileObj = open(file, 'a+', 1) #改为行缓冲
        sys.stdout = self.fileObj

    def toMute(self): #抑制输出
        self.nulObj = open(os.devnull, 'w')
        sys.stdout = self.nulObj

    def restore(self):
        self.content = ''
        if self.memObj.closed != True:
            self.memObj.close()
        if self.fileObj.closed != True:
            self.fileObj.close()
        if self.nulObj.closed != True:
            self.nulObj.close()
        sys.stdout = self.savedStdout #sys.__stdout__


redirObj = RedirectStdout()
sys.stdout = redirObj #本句会抑制"Let's begin!"输出
print "Let's begin!"

#屏显'Hello World!'和'I am xywang.'(两行)
redirObj.toCons(); print 'Hello World!'; print 'I am xywang.'
#写入'How are you?'和"Can't complain."(两行)
redirObj.toFile(); print 'How are you?'; print "Can't complain."
redirObj.toCons(); print "What'up?"   #屏显
redirObj.toMute(); print '<Silence>'  #无屏显或写入
os.system('echo Never redirect me!')  #控制台屏显'Never redirect me!'
redirObj.toMemo(); print 'What a pity!' #无屏显或写入
redirObj.toCons(); print 'Hello?'    #屏显
redirObj.toFile(); print "Oh, xywang can't hear me" #该串写入文件
redirObj.restore()

print 'Pop up' #屏显

#本节替换sys.stdout的代码实现并不影响由os.popen()、os.system()或os.exec*()系列方法所创建进程的标准I/O流。