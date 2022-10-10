import json
import os
import requests
import sys

sys.path.insert(0, '')

from crontab import CronTab
from dotenv import load_dotenv

load_dotenv()

INSTAGRAM_PAGE_ID = os.getenv('INSTAGRAM_PAGE_ID')
GRPAH_API_TOKEN = os.getenv('GRPAH_API_TOKEN')
CRON = CronTab(user=True)


def createInstagramTestPost():
    TEST_CAPTION = 'This is a test post.'

    image_location = 'https://cleanyour.shoes/wp-content/uploads/2022/08/Test-Post.jpg'
    post_url = 'https://graph.facebook.com/v14.0/{}/media'.format(INSTAGRAM_PAGE_ID)

    payload = {
        'image_url': image_location,
        'caption': TEST_CAPTION,
        'access_token': GRPAH_API_TOKEN
    }
    r = requests.post(post_url, data=payload)
    print(r.text)

    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']

        second_url = 'https://graph.facebook.com/v14.0/{}/media_publish'.format(INSTAGRAM_PAGE_ID)
        second_payload = {
            'creation_id': creation_id,
            'access_token': GRPAH_API_TOKEN
        }
        r = requests.post(second_url, data=second_payload)

        print('--------Successfully posted test post to IG--------')
        print(r.text)


    else:
        print('Test post unsuccessful. Please see log for errors.')

def schedulePost(image_location, caption, scheduled_time):
    job = CRON.new(command=createPost(image_location, caption, scheduled_time))
    job.setall(scheduled_time)

    if CRON[0].is_valid():
        CRON.write()

def createPost(image_location, caption, scheduled_time):
    post_url = 'https://graph.facebook.com/v14.0/{}/media'.format(INSTAGRAM_PAGE_ID)

    payload = {
        'image_url': image_location,
        'caption': caption,
        'access_token': GRPAH_API_TOKEN
    }

    r = requests.post(post_url, data=payload)
    print(r.text)

    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']

        second_url = 'https://graph.facebook.com/v14.0/{}/media_publish'.format(INSTAGRAM_PAGE_ID)
        second_payload = {
            'creation_id': creation_id,
            'access_token': GRPAH_API_TOKEN
        }
        r = requests.post(second_url, data=second_payload)

        # discordbot.sendMessageToDiscord('Successfully posted content to Instagram: {}'.format(image_location))
        # discordbot.sendMessageToDiscord('Post scheduled with CRON time: {}'.format(scheduled_time))

        print('--------Successfully posted test post to IG--------')
        print('Post made to Instagram scheduled with CRON time: {}'.format(scheduled_time))
        print(r.text)
    else:
        # discordbot.sendMessageToDiscord('Could not post content to Instagram: {}'.format(image_location))
        # discordbot.sendMessageToDiscord('Post scheduled with CRON time: {}'.format(scheduled_time))

        print('Test post unsuccessful. Please see log for errors.')

# def createInstagramTestPost(image_url):
