#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: The driver script to collect and analyze post information across reddits of varying ideologies

    Version: Python 2.7
    Requirements: Bot.py, Spreadsheet.py, Reddit.py and openpyxl """

from POL193_RedditBot.Bot import Bot

def print_subreddits(bot):
    for subreddit in bot.subreddits:
        print(unicode(subreddit.name) + ' | Users: ' + str(subreddit.users) + ' | Posts: ' +
              str(len(subreddit.top_posts)) + '\n---------------------------')
        for post in subreddit.top_posts:
            print unicode(post)
            print('')
        print "---------------------------"

def main():
    bot = Bot('193bot')
    bot.get_subreddits()
    bot.get_posts(20)
    bot.get_users(user_count=100, comment_count=100)
    bot.create_subreddit_output()
    bot.create_user_output()

if __name__ == '__main__':
    main()