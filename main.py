import os
import re
from random import shuffle

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from praw import Reddit
from vk import get_group, set_access_token
from vk.photos import Photo

import config

sched = BlockingScheduler()

# прочитай про авторизацию приложений в ВК
# и заполни сам

# авторизация в reddit
reddit =
hot_limit = 20

# придумай регулярку, фильтрующую изображения
pattern = re.compile(r"??????")

prefix = '#ithumor@lambdait'
hour = 16
minute = 10


def get_attachment(post):
    """
    Сотри pass и напиши нужный код ;)
    """
    pass


# Разкомментируй эту функцию, когда будешь заливать на heroku
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=hour, minute=minute)
# def post_to_vk():
#     pass

# sched.start()

if __name__ == "__main__":
    # получи нужный сабреддит
    subreddit =

    # собери топ постов
    hot =

    # придумай, что делать дальше :)