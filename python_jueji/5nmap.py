# -*- coding: utf8-*-
__author__ = 'Administrator'

import nmap

nmScan = nmap.PortScanner()
a = '80'
b = '210.51.19.61'
results = nmScan.scan(b,a)


print(results)
# {'nmap': {'scanstats': {'uphosts': '1', 'timestr': 'Mon Jul 11 06:44:35 2016', 'downhosts': '0', 'totalhosts': '1', 'elapsed': '27.97'}, 'scaninfo': {'tcp': {'services': '80', 'method': 'syn'}}, 'command_line': 'nmap -oX - -p 80 -sV 210.51.19.61'}, 'scan': {'210.51.19.61': {'status': {'state': 'up', 'reason': 'echo-reply'}, 'hostnames': [], 'vendor': {}, 'addresses': {'ipv4': '210.51.19.61'}, 'tcp': {80: {'product': 'nginx', 'state': 'open', 'version': '1.6.0', 'name': 'http', 'conf': '10', 'extrainfo': '', 'reason': 'syn-ack', 'cpe': 'cpe:/a:igor_sysoev:nginx:1.6.0'}}}}}
print(b +' '+ a+' ' + results['scan'][b]['tcp'][int(a)]['state'])
