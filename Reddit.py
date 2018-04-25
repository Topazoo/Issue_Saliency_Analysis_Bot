#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Classes to contain and organize subreddit data for a particular subreddit

    Version: Python 2.7 """

class Subreddit(object):
    """ Class to hold subreddit information """

    def __init__(self, name=None, ideology=None):
        self.name = name
        self.ideology = ideology
        self.users = 0
        self.top_posts = []
        self.top_posters = []

    def __str__(self):
        if self.name:
            return 'Name: ' + self.name + '\n Ideology: ' + self.ideology + '\n Users: ' + str(self.users)
        else:
            return 'Empty_Subreddit'

    def __repr__(self):
        if self.name:
            return self.name

        return 'Subreddit_Object'

class Post(object):

    def __init__(self, title=None, poster=None):
        self.poster = poster
        self.title = title
        self.type = None
        self.comments = 0
        self.up_votes = 0
        self.down_votes = 0

    def __str__(self):
        if self.title:
            return 'Title: ' + self.title + '\n Poster: ' + self.poster
        else:
            return "Empty_Post"

    def __repr__(self):
        if self.title:
            return self.title

        return 'Post_Object'

class User(object):

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