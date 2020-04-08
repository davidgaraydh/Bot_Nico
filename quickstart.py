""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run

insta_username = 'xxxxxxx'
insta_password = 'xxxxxxxxxxxxxx'
#followers = []


session=InstaPy(username=insta_username, 
        password=insta_password)

with smart_run(session):
       #session.follow_user_followers(['chicasemedesnudas10'], amount=50, randomize=False, sleep_delay=60)
       session.follow_by_tags(['teen', 'doloreshidalgogto'], amount=20)
       #session.story_by_tags(['maquillajeprofesional', 'hombres'])
       ##session.story_by_users(['eminem', 'calibre50oficial','luisitocomunica'])
        #insta_another_users=session.get_followers_anothers(['chicasemedesnudas10'], amount=10, randomize=False, sleep_delay=60)
       #session.unfollow_users(amount=84, custom_list_enabled=True, custom_list=custom_list, custom_list_param="all", style="RANDOM", unfollow_after=55*60*60, sleep_delay=600)
