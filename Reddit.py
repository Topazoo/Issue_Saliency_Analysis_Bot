#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Classes to contain and organize subreddit data for a particular subreddit

    Version: Python 2.7 """

class Subreddit(object):
    """ Class to hold subreddit information """

    def __init__(self, name, ideology):
        self.name = name
        self.ideology = ideology
        self.users = 0
        self.top_posts = []
        self.top_posters = []

    def __str__(self):
        return 'Name: ' + self.name + '\n Ideology: ' + self.ideology + '\n Users: ' + str(self.users)

    def __repr__(self):
        return self.name

class Post(object):

    def __init__(self):
        self.poster = None
        self.type = None
        self.comments = 0
        self.up_votes = 0
        self.down_votes = 0

class User(object):

    def __init__(self):
        self.name = None
        self.posts = 0
        self.karma = 0
        self.age = 0

        self.subreddits = []
        self.post_urls = []
