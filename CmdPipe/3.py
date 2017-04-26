#!python2
#coding:utf-8

#logging模块重定向
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s [%(levelname)s] at %(filename)s,%(lineno)d: %(message)s',
    datefmt = '%Y-%m-%d(%a)%H:%M:%S',
    filename = 'out.txt',
    filemode = 'w')


#将大于或等于INFO级别的日志信息输出到StreamHandler(默认为标准错误)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)-8s] %(message)s') #屏显实时查看，无需时间
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.debug('gubed'); logging.info('ofni'); logging.critical('lacitirc')
