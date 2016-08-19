#coding = UTF-8

import os
import _winreg
__author__ = 'Administrator'


def returnDir():
    dirs = ['c:\\Recycler\\', 'c:\\Recycled\\', 'c:\\$Recycle.Bin\\']
    for dirname in dirs:
        if os.path.isdir(dirname):
            return dirname

    return None


# 用Python 将用户的SID 关联起来
# 我们将使用Windows 注册表将SID 转化为一个准确的用户名。通过检查
# Windows 注册表键值HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows
# NT\CurrentVersion\ProfileList\<SID>\ProfileImagePath，我们可以看到它返回
# 一个是%SystemDrive%\Documents and Settings\<USERID>。在下图中，我
# 们看到这允许我们将SID 为S-1-5-21-1275210071-1715567821-725345543-
# 1005 转化为用户名“alex”。
def sid2user(sid):
        try:
            key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)
            (value, type) = _winreg.QueryValueEx(key, "ProfileImagePath")
            user = value.split('\\')[-1]
            return user
        except:
            return sid


def findRecycled(dirname):
    dirList = os.listdir(dirname)
    for sid in dirList:
        files = os.listdir(dirname + sid)
        user = sid2user(sid)
        print('[+]Listing files for ' + str(user) + ':')
        for filename in files:
            print('   ' + str(filename))


def main():
    recycleDir = returnDir()
    findRecycled(recycleDir)

if __name__ == '__main__':
    main()













