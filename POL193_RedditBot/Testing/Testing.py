#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: Unittests

    Version: Python 2.7 """

import os
from unittest import TestCase
from Code.POL193_RedditBot.Bot import Bot
from Code.POL193_RedditBot.Reddit import Subreddit, User
from Code.POL193_RedditBot.Spreadsheet import Spreadsheet

# Test Reddit Classes
class TestSubreddit(TestCase):
    def test_empty(self):
        subreddit = Subreddit()
        user = User()

        self.assertEqual(str(subreddit), 'Empty_Subreddit')
        self.assertEqual(repr(subreddit), '<Empty_Subreddit_Object>')
        self.assertEqual(str(user), 'Empty_User')
        self.assertEqual(repr(user), '<Empty_User_Object>')

    def test_full(self):
        subreddit = Subreddit('r/politics', 'Center')
        user = User('Peter')

        self.assertEqual(str(subreddit), 'Name: r/politics\n Ideology: Center\n Users: 0')
        self.assertEqual(repr(subreddit), 'r/politics')
        self.assertEqual(str(user), 'Name: Peter')
        self.assertEqual(repr(user), 'Peter')

# Test Spreadsheet Class
class TestSpreadsheet(TestCase):

    def test_write(self):
        file = 'test.xlsx'
        spreadsheet = Spreadsheet(file, False)
        self.assertTrue(os.path.isfile(file))
        spreadsheet.sheet['A2'] = "Test"
        self.assertTrue(spreadsheet.sheet['A2'].value, "Test")
        os.remove(file)

    def test_read_write_column(self):
        file = "col_write_test.xlsx"
        values = ["1", "2", "3", "Hello", "World"]
        spreadsheet = Spreadsheet(file, False)
        self.assertTrue(os.path.isfile(file))
        spreadsheet.write_column(1, values)
        results = spreadsheet.read_column(1, False)
        values = [unicode(x) for x in values]
        self.assertEqual(values, results.values()[0])
        os.remove(file)

    def test_read_write_row(self):
        file = "col_write_test.xlsx"
        values = ["1", "2", "3", "Hello", "World"]
        spreadsheet = Spreadsheet(file, False)
        self.assertTrue(os.path.isfile(file))
        spreadsheet.write_row(1, values)
        results = spreadsheet.read_row(1)
        values = [unicode(x) for x in values]
        self.assertEqual(values, results.values()[0])
        os.remove(file)

# Test Bot Class
class TestBot(TestCase):
    def test_read_input(self):
        bot = Bot('193bot')
        bot.get_subreddits()
        self.assertEqual([str(repr(x)) for x in bot.subreddits], [u'r/socialism', u'r/Libertarian', u'r/The_Donald', u'r/politics'])

    def test_get_posts(self):
        bot = Bot('193bot')
        bot.get_subreddits()
        bot.get_posts(10)

        flag = 0

        for subreddit in bot.subreddits:
            if len(subreddit.top_posts) < 8:
                flag = 1

        self.assertTrue(flag == 0)