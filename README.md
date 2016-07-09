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
