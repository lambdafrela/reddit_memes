# -*- coding: utf-8 -*-

import os
import configparser

config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'praw.ini')

try:
    config.read(config_file)
except configparser.ParsingError as e:
    print(e)
else:
    try:
        VK_ACCESS_TOKEN = config['VK']['ACCESS_TOKEN']
        VK_GROUP = config['VK']['GROUP']
    except KeyError:
        VK_ACCESS_TOKEN = os.environ.get('VK_ACCESS_TOKEN')
        VK_GROUP = os.environ.get('VK_GROUP')
