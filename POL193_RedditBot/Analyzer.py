#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Class to analyze Reddit information

    Version: Python 2.7 """

from textblob import TextBlob

class Analyzer(object):
    def __init__(self, subreddits):
        self.subreddits = subreddits

    def analyze_user_text(self):
        """ Record the subjectivity and polarity of all comments made by a user on a subreddit """

        for subreddit in self.subreddits:
            for user in subreddit.top_posters:
                all_user_text = ""
                # For every comment a user made on a subreddit
                for comment in user.sub_comments:
                    plus_ws = str(comment.text.encode('ascii', 'ignore')) + ' '
                    blob = TextBlob(plus_ws)

                    # Record polarity and subjectivity
                    comment.polarity = blob.polarity
                    comment.subjectivity = blob.subjectivity
                    user.average_polarity += blob.polarity
                    user.average_subjectivity += blob.subjectivity

                    all_user_text += plus_ws

                # Calculate averages
                try:
                    user.average_polarity = user.average_polarity / len(user.sub_comments)
                except ZeroDivisionError:
                    user.average_polarity = 0
                try:
                    user.average_subjectivity = user.average_subjectivity / len(user.sub_comments)
                except ZeroDivisionError:
                    user.average_subjectivity = 0

                # Record measurements for combined info
                blob = TextBlob(all_user_text)
                user.overall_polarity = blob.polarity
                user.overall_subjectivity = blob.subjectivity

    def analyze_subreddit_text(self):
        """ Record the subjectivity and polarity of all comments in a subreddit """

        for subreddit in self.subreddits:
            all_subreddit_text = ""
            # For all comments made in a subreddit
            for user in subreddit.top_posters:
                for comment in user.sub_comments:
                    plus_ws = str(comment.text.encode('ascii', 'ignore')) + ' '
                    blob = TextBlob(plus_ws)

                    # Record polarity and subjectivity
                    comment.polarity = blob.polarity
                    comment.subjectivity = blob.subjectivity
                    subreddit.average_polarity += blob.polarity
                    subreddit.average_subjectivity += blob.subjectivity

                    all_subreddit_text += plus_ws

            # Calculate averages
            try:
                subreddit.average_polarity = subreddit.average_polarity / sum([len(x.sub_comments) for x in subreddit.top_posters])
            except ZeroDivisionError:
                subreddit.average_polarity = 0
            try:
                subreddit.average_subjectivity = subreddit.average_subjectivity / sum([len(x.sub_comments) for x in subreddit.top_posters])
            except ZeroDivisionError:
                subreddit.average_subjectivity = 0

            # Record measurements for combined info
            blob = TextBlob(all_subreddit_text)
            subreddit.overall_polarity = blob.polarity
            subreddit.overall_subjectivity = blob.subjectivity

    def analyze_all_text(self):
        self.analyze_user_text()
        self.analyze_subreddit_text()