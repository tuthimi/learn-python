# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
