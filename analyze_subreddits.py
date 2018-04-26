#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: The driver script to collect and analyze post information across reddits of varying ideologies

    Version: Python 2.7
    Requirements: Bot.py, Spreadsheet.py, Reddit.py and openpyxl """

from Bot import Bot

def main():
    bot = Bot()
    bot.get_subreddits()
    bot.analyze_subreddits(10)

    for subreddit in bot.subreddits:
        print(unicode(subreddit.name) + ' - ' + str(len(subreddit.top_posts)) + '\n---------------------------')
        for post in subreddit.top_posts:
            print unicode(post)
        print "---------------------------"

if __name__ == '__main__':
    main()