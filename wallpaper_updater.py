#!/usr/local/bin/python3.5
import praw
import urllib
import os
from apscheduler.schedulers.background import BackgroundScheduler
import time
import sched


def update_background(sc): 
    # do your stuff
    change_background()
    sc.enter(3600, 1, update_background, (sc,))

def change_background():
    #user agent setup
    user_agent_string = 'put_a_unique_user_name_here'
    user_agent = praw.Reddit(user_agent = user_agent_string)

    #get top post from earth porn
    top_posts = user_agent.get_subreddit('earthporn').get_hot(limit = 5)
    for post in top_posts:
        url = post.url
        
        #get image
        fname = url.split('/')[-1]
        if '.jpg' in fname:
            urllib.request.urlretrieve(url,os.path.expanduser('~')+'/.wallpaper_updater/wallpaper_updater.jpg')
            break
        elif 'imgur' in url:
            # imgur links look like this 
            # http://imgur.com/77PaCzo
            # the photos look like this
            # http://i.imgur.com/77PaCzo.jpg
            url = 'http://i.imgur.com/'+fname +'.jpg'
            urllib.request.urlretrieve(url,os.path.expanduser('~')+'/.wallpaper_updater/wallpaper_updater.jpg')
            break
        
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        
if __name__ == '__main__':
    ensure_dir(os.path.expanduser('~')+'/.wallpaper_updater/')
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, update_background, (s,))
    s.run()
