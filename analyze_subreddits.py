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

    print(bot.subreddits)

if __name__ == '__main__':
    main()