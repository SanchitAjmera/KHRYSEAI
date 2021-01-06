from instapy import InstaPy
import sys

#===============================CONFIGURATION===============================#

# Credentials
userName = "burner123490"
passWord = "burner1234"

# Tags targeted
tags = [sys.argv[1]]

# Volume of posts targeted
volume = 1

# Comments
comments = ["comment1","comment2","comment3","comment4","comment5","comment6","comment7","comment8","comment9","comment10"]

# Delays in seconds
comment_delay = 3
like_delay = 3

#===============================CONFIGURATION===============================#


session = InstaPy(username=userName, password=passWord)

session.set_quota_supervisor(enabled=True, peak_comments_daily=90, peak_comments_hourly=10)
session.set_action_delays(enabled=True, like=like_delay, comment=comment_delay)
session.login()

session.set_dont_like(["naked", "nsfw"])

session.set_do_follow(True, percentage=0)

session.set_do_comment(True, percentage=100)
session.set_comments(comments)

session.like_by_tags(tags, amount=volume)

session.end()