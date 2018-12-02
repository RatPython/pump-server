#!/usr/bin/env python3

import configparser
import sqlite3
import os.path
import os
import shutil

# dd533b39dff5b11ef6f88915c4db29eac2af137a
# Конфиг. Может лежать где угодно, в принципе
configFileName = '/home/mt/pump/pump-server/pump-server.conf'

cfg = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
# cfg = configparser.ConfigParser()

cfg.read(configFileName)

db = cfg.get('Database', 'db')
queueDir = cfg.get('Dirs', 'queue')


def createDatabase(dbFile, overwrite=False):
    fileExists = os.path.exists(dbFile)
    if fileExists and overwrite:
        os.remove(db)
    if not fileExists:
        pass
