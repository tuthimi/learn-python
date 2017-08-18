# coding: utf-8
#20170814 匹配web数据格式


"""命令行火车票查看器

Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h, --help 查看帮助
    -d         动车
    -g         高铁
    -k         快速
    -t         特快
    -z         直达

Examples:
    tickets 上海 北京 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""

import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init, Fore

from stations import stations

requests.packages.urllib3.disable_warnings()

init()

class TrainsCollection:

    header = '车次 车站 时间 历时 商务 一等 二等 高软 软卧 硬卧 硬座 无座'.split()

    def __init__(self, available_trains, options):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.split('|')[10].replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_no = raw_train.split('|')[3]
            # initial = train_no[0].lower()
            if True:
                train = [
                    train_no,        
                    '\n'.join([Fore.GREEN + dict_reverse_find(stations, raw_train.split('|')[4]) + Fore.RESET,
                               Fore.RED + dict_reverse_find(stations, raw_train.split('|')[5]) + Fore.RESET]),
                    '\n'.join([Fore.GREEN + raw_train.split('|')[8] + Fore.RESET,
                               Fore.RED + raw_train.split('|')[9] + Fore.RESET]),
                    self._get_duration(raw_train),
                    raw_train.split('|')[32],#商务座
                    raw_train.split('|')[31],#一等座,
                    raw_train.split('|')[30],#二等座,
                    raw_train.split('|')[21],#高级软卧
                    raw_train.split('|')[23],#软卧
                    raw_train.split('|')[28],#硬卧,
                    raw_train.split('|')[26],#硬座,
                    raw_train.split('|')[29],#无座,
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

def dict_reverse_find(mydic, wd):
    for key,value in mydic.items():
        if value == wd:
            return key

def cli():
    """Command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}'
           '&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
                date, from_station, to_station
           )

    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    r = requests.get(url, verify=False)
    #print(r.json())
    available_trains = r.json()['data']['result']
    TrainsCollection(available_trains, options).pretty_print()


if __name__ == '__main__':
    cli()