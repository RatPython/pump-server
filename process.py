#!/usr/bin/env python3

import configparser
import sqlite3
import os.path
import os
import logging
import shutil

# dd533b39dff5b11ef6f88915c4db29eac2af137a
# Конфиг. Может лежать где угодно, в принципе
configFileName = '/home/mt/pump/pump-server/pump-server.conf'
cfg = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
cfg.read(configFileName)


def openDatabase(dbFile, DDL, overwrite=False):
    """Открывает Sqlite - базу данных. В случае отсутствия - создает. :param
    string dbFile: файл базы данных :param string DDL: DDL-описание таблицы в
    виде строки :param boolean overwrite: True - пересоздать в случае, если файл
    БД существует. По умолочанию - False :return: sqlite3.Connection: - коннект
    к базе данных, или string - строка исключения

    Args:
        dbFile:
        DDL:
        overwrite:
    """
    fileExists = os.path.exists(dbFile)
    if fileExists and overwrite:
        os.remove(db)
    try:
        conn = sqlite3.connect(dbFile)
    except Exception as e:
        return str(e)


logName = cfg.get("Dirs", "processLog")
logging.basicConfig(format=u'%(asctime)s (%(process)d)  [%(filename)s (LINE:%(lineno)d)]# : %(message)s',
                    level=logging.DEBUG, filename=logName)

logging.info('+ Begin :')

db = cfg.get('Database', 'db')
logging.debug(' * db = [%s]' % db)

queueTableName = 'queue'
logging.debug(' * queueTableName = [%s]' % queueTableName)

queueTableDDL = cfg.get('Database', 'queueTable')
logging.debug(' * queueTableDDL = [%s]' % queueTableDDL)

queueDir = cfg.get('Dirs', 'queue')
logging.debug(' * queueDir = [%s]' % queueDir)

conn = openDatabase()
