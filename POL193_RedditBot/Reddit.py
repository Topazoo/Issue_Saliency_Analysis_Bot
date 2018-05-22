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
        self.most_frequent = []
        self.average_subjectivity = 0
        self.overall_subjectivity = None
        self.average_polarity = 0
        self.overall_polarity = None

    def __str__(self):
        if self.name and self.ideology:
            return 'Name: ' + self.name + '\n Ideology: ' + self.ideology + '\n Users: ' + str(self.users)
        return 'Empty_Subreddit'

    def __repr__(self):
        if self.name:
            return str(self.name)
        return '<Empty_Subreddit_Object>'

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

        return 'Empty_Post'

    def __repr__(self):
        if self.title:
            return self.title.encode('ascii', 'ignore')
        return '<Empty_Post_Object>'

class User(object):
    """ Class to hold user information """

    def __init__(self, name=None):
        self.name = name
        self.profile = None
        self.average_subjectivity = 0
        self.overall_subjectivity = None
        self.average_polarity = 0
        self.overall_polarity = None

        self.sub_comments = []
        self.most_frequent = []

    def get_comments(self, subreddit, num_comments=10):
        """ Collects recent posts by a user in a given subreddit
            @subreddit - The subreddit to get comments from
            @num_comments - The number of comments to record """

        comment_num = 0
        for comment in self.profile.comments.new(limit=num_comments):
            if comment_num == num_comments:
                break
            if str(comment.subreddit.display_name) == str(subreddit.name[2:]):
                # Create and store comment object
                com = Comment(comment)
                self.sub_comments.append(com)
                comment_num += 1

    def __str__(self):
        if self.name:
            return 'Name: ' + self.name
        return "Empty_User"

    def __repr__(self):
        if self.name:
            return str(self.name)
        return '<Empty_User_Object>'

class Comment(object):
    """ Class to hold comment information """

    def __init__(self, comment):
        self.author = comment.author
        self.text = comment.body
        self.post = comment.submission
        self.polarity = None
        self.subjectivity = None
        self.most_frequent = []

    def __str__(self):
        if self.author and self.text:
            return self.text.encode('ascii', 'ignore')
        return ""

    def __repr__(self):
        if self.author:
            return '<Comment: Author=' + self.author.encode('ascii', 'ignore') +'>'
        return '<Empty_User_Object>'
