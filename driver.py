#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: The driver script to collect and analyze post information across reddits of varying ideologies

    Version: Python 2.7
    Requirements: Bot.py, Spreadsheet.py, Reddit.py and openpyxl """

from POL193_RedditBot.Bot import Bot

def run_options():
    user_count = 10
    comment_count = 30
    post_count = 20
    create_output = True
    analyze = True

    inpt = -1

    while inpt != "" and inpt != "\n" and inpt != "c":
        inpt = str(raw_input("Press enter to run with default options, or \'c\' to run with custom options\n>>> "))

    if inpt == "c":
        while inpt != "y" and inpt != "n":
            inpt = str(raw_input("Create output [y/n] >>> "))
        if inpt == "n":
            create_output = False
        inpt = -1
        while inpt != "y" and inpt != "n":
            inpt = str(raw_input("Analyze data [y/n] >>> "))
        if inpt == "n":
            analyze = False
        while not inpt.isdigit() or int(inpt) < 0:
            inpt = str(raw_input("Enter a number of posts to analyze >>> "))
        post_count = int(inpt)
        inpt = ""
        while not inpt.isdigit() or int(inpt) < 0:
            inpt = str(raw_input("Enter a number of users to analyze >>> "))
        user_count = int(inpt)
        inpt = ""
        while not inpt.isdigit() or int(inpt) < 0:
            inpt = str(raw_input("Enter a number of comments to analyze >>> "))
        comment_count = int(inpt)

        print("Running with custom options. Please wait...")
    else:
        print("Running with default options. Please wait...")

    return (post_count, user_count, comment_count, create_output, analyze)




def main():

    options = run_options()

    bot = Bot('193bot')
    bot.get_subreddits()
    bot.get_posts(options[0])
    bot.get_users(options[1], options[2])

    if options[3]:
        bot.create_subreddit_output()
        bot.create_user_output()

    if options[4]:
        bot.analyze()

if __name__ == '__main__':
    main()