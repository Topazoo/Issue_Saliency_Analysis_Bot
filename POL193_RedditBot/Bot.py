#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: A class to contain, organize, and analyze Reddit data

    Version: Python 2.7
    Requirements: Spreadsheet.py, Reddit.py and openpyxl """

import praw

from Reddit import Subreddit, Post
from Spreadsheet import Spreadsheet

class Bot(object):
    """ Class to contain highest-order program operations """

    def __init__(self):
        # Open spreadsheets for inputs and results
        self.input_sheet = Spreadsheet("input/subreddits.xlsx")
        self.output_file = Spreadsheet("output/results.xlsx", False)

        self.reddit = praw.Reddit('193bot')

        # Create a list of subreddits
        self.subreddits = []

    def get_subreddits(self):
        """ Get info from the spreadsheet """

        # Get subreddit names
        subreddits_column = self.input_sheet.read_column(1)

        # Get subreddit ideologies
        ideology_column = self.input_sheet.read_column(1)

        # Zip and store combined information
        subreddits = zip(subreddits_column.values()[0], ideology_column.values()[0])

        for subreddit in subreddits:
            subreddit_obj = Subreddit(subreddit[0], subreddit[1])
            subreddit_obj.feed = self.reddit.subreddit(subreddit[0][2:])
            subreddit_obj.users = subreddit_obj.feed.subscribers
            self.subreddits.append(subreddit_obj)

    def get_posts(self, limit=30, range='year'):
        """ Get a number (limit) of top posts ranging back a range.
            @Params:
             limit - number of posts to collect
             range - range of time to get posts from """

        # For all subreddits, collect valid posts
        for subreddit in self.subreddits:
            for post in subreddit.feed.top(range, limit=limit):
                post_object = Post(post)
                if post_object.title and post_object.poster:
                    subreddit.top_posts.append(post_object)

    def get_users(self):
        # Most active now
        ## Last 100 posts and the users posting in the comments
        # Most active a year ago
        # Moderators
        test = "test"