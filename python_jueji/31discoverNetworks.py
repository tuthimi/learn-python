# coding=UTF-8
#读注册表

__author__ = 'Administrator'

import _winreg

def val2addr(val):
    addr = ''
    for ch in val:
        addr += ("%02x " % ord(ch))
        addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr

def printNets():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    #net = "SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces"

    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, net)
    print('Networks you have joined:')
    for i in range(100):
        try:
            guid = _winreg.EnumKey(key, i)
            netKey = _winreg.OpenKey(key, str(guid))
            (n, addr, t) = _winreg.EnumValue(netKey, 5)
            (n, name, t) = _winreg.EnumValue(netKey, 4)
            Netaddr = val2addr(addr)
            Netname = str(name)
            print('[+]' + Netaddr + ' '+ Netname)
            _winreg.CloseKey(netKey)
        except Exception as e:
            print e
            break

def main():
    printNets()

if __name__ == '__main__':
    main()