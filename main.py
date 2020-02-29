#!/usr/bin/python3
import logging
import sys
import configparser

from rssbot import RSSBot

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('conf.ini')
    
    if config.get("default", "loglevel") == 'ERROR':
        _level = logging.ERROR
    elif config.get("default", "loglevel") == 'INFO':
        _level = logging.INFO
    else:
        _level = logging.DEBUG

    _format = '%(filename)s[line:%(lineno)d]: %(message)s'
    logging.basicConfig(level=_level, format=_format)

    bot = RSSBot()
    bot.run()
