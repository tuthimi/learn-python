#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'

if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":212}
    mm='li'
    for m in person:
        if person[mm] < person[m]:
            mm = m

    print '%s,%d' % (mm,person[mm])
