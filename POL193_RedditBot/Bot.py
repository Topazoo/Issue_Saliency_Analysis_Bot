#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: A class to contain, organize, and analyze Reddit data

    Version: Python 2.7
    Requirements: Spreadsheet.py, Reddit.py, Analyzer.py, praw and openpyxl """

import praw
from collections import Counter
from Reddit import Subreddit, Post, User
from Spreadsheet import Spreadsheet
from Analyzer import Analyzer

class Bot(object):
    """ Class to contain highest-order program operations
        @bot_name - The name of the Praw bot """

    def __init__(self, bot_name='193bot'):
        # Open spreadsheets for inputs and results
        self.input_sheet = Spreadsheet("input/subreddits.xlsx")
        self.subreddit_output_sheet = Spreadsheet("output/subreddit_results.xlsx", False)
        self.user_output_sheet = Spreadsheet("output/user_results.xlsx", False)
        self.comment_output_sheet = Spreadsheet("output/comment_results.xlsx", False)

        self.reddit = praw.Reddit(bot_name)

        # Create a list of subreddits
        self.subreddits = []

        # Class to analyze collected information
        self.analyzer = Analyzer(self.subreddits)

    def get_subreddits(self):
        """ Get info from the spreadsheet """

        # Get subreddit names
        subreddits_column = self.input_sheet.read_column(1)

        # Get subreddit ideologies
        ideology_column = self.input_sheet.read_column(2)

        # Zip and store combined information
        subreddits = zip(subreddits_column.values()[0], ideology_column.values()[0])

        for subreddit in subreddits:
            subreddit_obj = Subreddit(subreddit[0], subreddit[1])
            subreddit_obj.feed = self.reddit.subreddit(subreddit[0][2:])
            subreddit_obj.users = subreddit_obj.feed.subscribers
            self.subreddits.append(subreddit_obj)

    def get_posts(self, limit=30, range='year'):
        """ Get a number (limit) of top posts ranging back a range.
             @limit - number of posts to collect
             @range - range of time to get posts from """

        # For all subreddits, collect valid posts
        for subreddit in self.subreddits:
            for post in subreddit.feed.top(range, limit=limit):
                post_object = Post(post)
                if post_object.title and post_object.poster:
                    subreddit.top_posts.append(post_object)

    def create_subreddit_output(self):
        """ Create the subreddit output file """

        # Create sheets
        init_sheet = self.subreddit_output_sheet.file['Sheet']
        init_sheet.title = 'Subreddits'
        self.subreddit_output_sheet.create_sheets([repr(x)[2:] for x in self.subreddits])

        self.write_subreddits()
        self.write_posts()

        print("Success! Data written to: output/subreddit_results.xlsx")

    def create_comment_output(self):
        """ Create the comment output file """

        # Create sheets
        init_sheet = self.comment_output_sheet.file['Sheet']
        init_sheet.title = 'Subreddits'
        self.comment_output_sheet.create_sheets([repr(x)[2:] for x in self.subreddits])

        self.write_comments()

        print("Success! Data written to: output/coment_results.xlsx")


    def create_user_output(self):
        """ Create the output sheet for user information """

        init_sheet = self.user_output_sheet.file['Sheet']
        init_sheet.title = 'Users'
        self.user_output_sheet.create_sheets([repr(x)[2:] for x in self.subreddits])

        self.write_user_info()
        self.write_users()

        print("Success! Data written to: output/user_results.xlsx")

    def write_subreddits(self):
        """ Write subreddit info to subreddit sheet """

        # Dynamically create legend based on current attributes of the Subreddit class
        self.subreddit_output_sheet.write_row(1, [str(x).title() for x in sorted(self.subreddits[0].__dict__.keys(), reverse=True)
                                                  if x != "feed" and x != "top_posts"], start_col=1, bold=True)

        # Dynamically write info for subreddits based on the current attributes of the Subreddit class
        sub_num = 2
        for subreddit in self.subreddits:
            self.subreddit_output_sheet.write_row(sub_num, [str(x[1]) for x in sorted(subreddit.__dict__.items(),
                                                                                      key=lambda att: att[0], reverse=True)
                                                            if x[0] != "feed" and x[0] != "top_posts"], start_col=1)
            sub_num += 1

    def write_posts(self):
        """ Write posts to subreddit sheet """

        # Loop through each sheet and write a dynamic legend based on the current attributes of the Post class
        sub_num = 0
        for sheet in self.subreddit_output_sheet.file.worksheets:
            if str(sheet.title) != "Subreddits":
                self.subreddit_output_sheet.sheet = sheet
                self.subreddit_output_sheet.write_row(1,[str(x).title() for x in self.subreddits[0].top_posts[0].__dict__.keys() if x != "post"],
                                            start_col=1, bold=True)

                # Dynamically write all current values of the Post class (write all relevent post data for all posts)
                row_num = 2
                for post in self.subreddits[sub_num].top_posts:
                    self.subreddit_output_sheet.write_row(row_num, [str(x[1]) for x in post.__dict__.items() if x[0] != "post"], start_col=1)
                    row_num += 1

                sub_num += 1

    def write_users(self):
        """ Write comments for each user """

        sub_num = 0
        for sheet in self.user_output_sheet.file.worksheets:
            if str(sheet.title) != "Users":
                self.user_output_sheet.sheet = sheet

                # Write all posts
                user_num = 1
                for user in self.subreddits[sub_num].top_posters:
                    # Write all usernames
                    self.user_output_sheet.write_row(1, [user.name], user_num, bold=True)
                    # Write subheadings
                    self.user_output_sheet.write_row(2, ["Post", "Polarity", "Subjectivity"], user_num, italics=True)
                    # Write comments
                    self.user_output_sheet.write_column(user_num, [comment.text.encode('ascii', 'ignore') for comment in user.sub_comments],
                                                        start_row=3)
                    # Write polarity
                    self.user_output_sheet.write_column(user_num + 1, [str(comment.polarity) for comment in
                                                                   user.sub_comments], start_row=3)
                    # Write subjectivity
                    self.user_output_sheet.write_column(user_num + 2, [str(comment.subjectivity) for comment in
                                                                       user.sub_comments], start_row=3)
                    user_num += 3

                sub_num += 1

    def write_user_info(self):
        """ Write info collected about users """

        # Get and label sheet
        self.user_output_sheet.sheet = self.user_output_sheet.file.worksheets[0]
        self.user_output_sheet.write_row(1,["User", "Karma", "Subreddit", "Comments", "Average Polarity", "Average Subjectivity", "Frequent Nouns"], bold=True)

        row = 2
        for subreddit in self.subreddits:
            # Write names
            self.user_output_sheet.write_column(1, [str(poster.name) for poster in subreddit.top_posters], start_row=row)
            # Write karma
            self.user_output_sheet.write_column(2, [str(poster.profile.comment_karma) for poster in subreddit.top_posters], start_row=row)
            # Write subreddits
            self.user_output_sheet.write_column(3, [str(subreddit.name)] * len(subreddit.top_posters), start_row=row)
            # Write comment count
            self.user_output_sheet.write_column(4, [str(len(poster.sub_comments)) for poster in subreddit.top_posters], start_row=row)
            # Write average polarity
            self.user_output_sheet.write_column(5, [str(poster.average_polarity) for poster in subreddit.top_posters], start_row=row)
            # Write average subjectivity
            self.user_output_sheet.write_column(6, [str(poster.average_subjectivity) for poster in subreddit.top_posters], start_row=row)
            # Write most used nouns
            self.user_output_sheet.write_column(7, [str(poster.most_frequent) for poster in subreddit.top_posters], start_row=row)

            row += len(subreddit.top_posters)

    def write_comments(self):
        """ Write info collected about comments """

        # Get sheet
        self.comment_output_sheet.sheet = self.comment_output_sheet.file.worksheets[0]

        # Write legend
        self.comment_output_sheet.write_row(2, ["Noun", "Frequency"] * len(self.subreddits), italics=True)

        # Write data
        col = 1
        for subreddit in self.subreddits:
            self.comment_output_sheet.write_column(col, [subreddit.name], bold=True)
            self.comment_output_sheet.write_column(col, [str(tup[0]) for tup in subreddit.most_frequent], start_row=3)
            self.comment_output_sheet.write_column(col+1, [str(tup[1]) for tup in subreddit.most_frequent], start_row=3)
            col += 2

        sub_num = 0
        for sheet in self.comment_output_sheet.file.worksheets:
            if str(sheet.title) != "Subreddits":
                user_col = 1
                self.comment_output_sheet.sheet = sheet
                self.comment_output_sheet.write_row(2, ["Noun", "Frequency"] * len(self.subreddits[sub_num].top_posters),
                                                    italics=True)
                for user in self.subreddits[sub_num].top_posters:
                    self.comment_output_sheet.write_column(user_col, [user.name], start_row=1, bold=True)
                    self.comment_output_sheet.write_column(user_col, [str(tup[0]) for tup in user.most_frequent], start_row=3)
                    self.comment_output_sheet.write_column(user_col+1, [str(tup[1]) for tup in user.most_frequent], start_row=3)
                    user_col += 2

                sub_num += 1

    def get_users(self, user_count=10, comment_count=10):
        """ Get the top users for each subreddit
            @user_count - The number of users to record
            @comment_count - The number of recent comments in a subreddit to record """

        for subreddit in self.subreddits:
            users = {}

            # Record posters of last 5000 comments
            for comment in subreddit.feed.comments(limit=5000):
                if comment.author:
                    if comment.author.name not in users.keys():
                        users[comment.author.name] = 1
                    else:
                        users[comment.author.name] += 1

            counter = Counter(users)
            # Get users that comment most frequently
            for user in counter.most_common(user_count):
                # Store as a user object
                new_user = User(user[0])
                new_user.profile = self.reddit.redditor(user[0])
                # Store most recent comments
                new_user.get_comments(subreddit, comment_count)
                subreddit.top_posters.append(new_user)

    def analyze(self, nouns_count=5):
        """ Analyze all text
            @nouns_count - The number of nouns to collect """

        self.analyzer.analyze_all_text(nouns_count)