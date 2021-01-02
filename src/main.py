from instapy import InstaPy

#===============================CONFIGURATION===============================#

# Credentials
username = ""
password = ""

# Tags targeted
tags = []

# Volume of posts targeted
volume = 5

# Comments
comments = []

# Delays

#===============================CONFIGURATION===============================#


session = InstaPy(username=username, password=password)

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=9)
session.set_action_delays(enabled=True, like=3, comment=5)
session.login()

session.like_by_tags(tags, amount=volume)
session.set_dont_like(["naked", "nsfw"])

session.set_do_follow(True, percentage=0)

session.set_do_comment(True, percentage=100)
session.set_comments(comments)



session.end()