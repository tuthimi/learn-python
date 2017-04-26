#python2
#coding:utf-8

import logging, logging.config

logging.config.fileConfig("logger.conf")

logger = logging.getLogger("Logger2CF")
logger.debug('gubed'); logger.info('ofni'); logger.warn('nraw')
logger.error('rorre'); logger.critical('lacitirc')

logger1 = logging.getLogger("Logger2F")
logger1.debug('GUBED'); logger1.critical('LACITIRC')

logger2 = logging.getLogger()
logger2.debug('gUbEd'); logger2.critical('lAcItIrC')
