import re
import os
import requests
import config

from praw import Reddit
from vk import set_access_token, get_group
from vk.photos import Photo
from random import choice, shuffle
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

set_access_token(config.VK_ACCESS_TOKEN)
group = get_group(config.VK_GROUP)

reddit = Reddit('bot1')
hot_limit = 20

pattern = re.compile(r"(jpe?g|png)|imgur")
prefix = '#ithumor@lambdait'

def download_attachment(attachment_url):
	response = requests.get(attachment_url, stream=True)
	return response.content


def get_attachment(post):
	binary_content = download_attachment(post.url)
	_, filename = os.path.split(post.url)
	yield (filename, binary_content)


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=15, minunte=30)
def post_to_vk():
	subreddit = reddit.subreddit('ProgrammerHumor')
	hot = list(subreddit.hot(limit=hot_limit))

	while len(hot) > 0:
		shuffle(hot)
		post = hot.pop()

		if re.findall(pattern, post.url):
			attachment_items = {filename: binary_content for filename, 
				binary_content in get_attachment(post)}
			photo_items = Photo.upload_wall_photos_for_group(int(VK_GROUP),
				attachment_items.items())
			group.wall_post(message=f'{prefix}\n\n{post.title}',
				attachments=photo_items)
			break

sched.start()
