#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Classes to contain and organize subreddit data for a particular subreddit

    Version: Python 2.7 """

import datetime

class Subreddit(object):
    """ Class to hold subreddit information """

    def __init__(self, name=None, ideology=None):
        self.name = name
        self.ideology = ideology
        self.feed = None
        self.users = 0
        self.top_posts = []
        self.top_posters = []

    def __str__(self):
        if self.name and self.ideology:
            return 'Name: ' + self.name + '\n Ideology: ' + self.ideology + '\n Users: ' + str(self.users)
        else:
            return 'Empty_Subreddit'

    def __repr__(self):
        if self.name:
            return str(self.name)
        return 'Subreddit_Object'

class Post(object):
    """ Class to hold post information """

    def __init__(self, post):
        self.post = post
        self.poster = post.author
        self.title = post.title.encode('ascii', 'ignore')
        self.comments = post.num_comments
        self.score = post.score
        self.up_votes = post.ups
        self.down_votes = post.downs
        self.date = post.created_utc
        self.url = post.url
        self.link = post.permalink
        self.type = self.get_type(post)
        self.text = None

        if post.selftext is not u'':
            self.text = post.selftext.encode('ascii', 'ignore')

    def get_type(self, post):
        """ Checks if a post has attached media """

        if 'youtube.com' in post.url or 'streamable.com' in post.url or 'vimeo.com' in post.url:
            return "Video"
        elif post.url.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')) or 'flickr.com' in post.url or \
                'imgur.com' in post.url:
            return "Image"
        elif post.url.lower().endswith(('.gif', 'gifv')) or "gfycat.com" in post.url:
            return "GIF"
        elif 'reddit.com' not in post.url:
            return "URL"
        else:
            return "Text"

    def __str__(self):
        if self.title and self.poster:
            string = 'Title: ' + self.title + '\n Poster: ' + self.poster.name.encode('ascii', 'ignore') + '\n Score: ' + \
                     str(self.score) + '\n Comments: ' + str(self.comments) + '\n Type: ' + self.type + '\n Date: ' + \
                     str(datetime.datetime.utcfromtimestamp(self.date)) + '\n Link: ' + self.link

            if self.text:
                string += ('\n Text: ' + self.text)

            return string
        else:
            return 'Empty_Post'

    def __repr__(self):
        if self.title:
            return self.title
        return 'Post_Object'

class User(object):
    """ Class to hold user information """

    def __init__(self, name=None):
        self.name = name
        self.posts = 0
        self.karma = 0
        self.age = 0

        self.subreddits = []
        self.post_urls = []

    def __str__(self):
        if self.name:
            return 'Name: ' + self.name
        else:
            return "Empty_User"

    def __repr__(self):
        if self.name:
            return self.name
        return 'User_Object'