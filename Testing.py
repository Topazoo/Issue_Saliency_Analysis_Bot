#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Unittests

    Version: Python 2.7 """

from unittest import TestCase
from Reddit import Subreddit, Post, User
from Spreadsheet import Spreadsheet
from Bot import Bot
import os

# Test Reddit Classes
class TestSubreddit(TestCase):
    def test_empty(self):
        subreddit = Subreddit()
        post = Post()
        user = User()

        self.assertEqual(str(subreddit), 'Empty_Subreddit')
        self.assertEqual(repr(subreddit), 'Subreddit_Object')
        self.assertEqual(str(post), 'Empty_Post')
        self.assertEqual(repr(post), 'Post_Object')
        self.assertEqual(str(user), 'Empty_User')
        self.assertEqual(repr(user), 'User_Object')

    def test_full(self):
        subreddit = Subreddit('r/politics', 'Center')
        post = Post('Hello Reddit', 'Peter')
        user = User('Peter')

        self.assertEqual(str(subreddit), 'Name: r/politics\n Ideology: Center\n Users: 0')
        self.assertEqual(repr(subreddit), 'r/politics')
        self.assertEqual(str(post), 'Title: Hello Reddit\n Poster: Peter')
        self.assertEqual(repr(post), 'Hello Reddit')
        self.assertEqual(str(user), 'Name: Peter')
        self.assertEqual(repr(user), 'Peter')

# Test Spreadsheet Class
class TestSpreadsheet(TestCase):
    def test_read_column(self):
        spreadsheet = Spreadsheet('subreddits.xlsx')
        column_0 = spreadsheet.read_column(0)
        self.assertEqual(column_0.keys()[0], 'Subreddit')
        self.assertEqual(column_0.values()[0], [u'r/socialism', u'r/Libertarian', u'r/The_Donald', u'r/politics'])
        os.remove('results.xlsx')

    def test_write(self):
        file = 'test.xlsx'
        spreadsheet = Spreadsheet(file, False)
        self.assertTrue(os.path.isfile(file))
        spreadsheet.sheet['A2'] = "Test"
        self.assertTrue(spreadsheet.sheet['A2'].value, "Test")
        os.remove(file)

# Test Bot Class
class TestBot(TestCase):
    def test_read_input(self):
        bot = Bot()
        bot.get_subreddits()
        self.assertEqual([str(repr(x)) for x in bot.subreddits], [u'r/socialism', u'r/Libertarian', u'r/The_Donald', u'r/politics'])
