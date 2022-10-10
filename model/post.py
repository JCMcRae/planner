# The scheduled post time is in CRON because it's easier to schedule posts that way.
class Post:
    def __init__(self, image_url, caption, scheduled_post_time = "* * * * *"):
        self.image_url = image_url
        self.caption = caption
        self.scheduled_post_time = scheduled_post_time