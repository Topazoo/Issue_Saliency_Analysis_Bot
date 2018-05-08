#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Class to analyze Reddit information

    Version: Python 2.7 """

class Analyzer(object):
    def __init__(self, subreddits):
        self.subreddits = subreddits
        self.text_samples_user = {}
        self.text_samples_subreddit = {}

    def get_text_samples_user(self):
        """ Combine all text based on user """

        for subreddit in self.subreddits:
            for user in subreddit.top_posters:
                self.text_samples_user[str(user.name)] = ""
                for comment in user.sub_comments:
                    self.text_samples_user[str(user.name)] += (comment.text.encode('ascii', 'ignore') + ' ')

    def get_text_samples_subreddit(self):
        """ Combine all text based on subreddit """

        for subreddit in self.subreddits:
            self.text_samples_subreddit[str(subreddit.name.encode('ascii', 'ignore'))] = ""
            for user in subreddit.top_posters:
                for comment in user.sub_comments:
                    plus_ws = str(comment.text.encode('ascii', 'ignore')) + ' '
                    self.text_samples_subreddit[str(subreddit.name.encode('ascii', 'ignore'))] += plus_ws

    def analyze_user_text(self):
        self.get_text_samples_user()

    def analyze_subreddit_text(self):
        self.get_text_samples_subreddit()

    def analyze_all_text(self):
        self.analyze_user_text()
        self.analyze_subreddit_text()