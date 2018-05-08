#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: The driver script to collect and analyze post information across reddits of varying ideologies

    Version: Python 2.7
    Requirements: Bot.py, Spreadsheet.py, Reddit.py and openpyxl """

from POL193_RedditBot.Bot import Bot

class Driver(object):
    def __init__(self):
        self.post_count = 20
        self.user_count = 10
        self.comment_count = 30
        self.create_output = True
        self.analyze = True

        if self.custom_options():
            self.post_count = self.get_pos_int("posts")
            self.user_count = self.get_pos_int("users")
            self.comment_count = self.get_pos_int("comments")
            self.create_output = self.get_y_n("Create output")
            self.analyze = self.get_y_n("Analyze data")

            print("Running with custom options. Please wait...")
        else:
            print("Running with default options. Please wait...")

    def custom_options(self):
        """ Prompt the user for default or custom options """

        inpt = -1

        while inpt != "" and inpt != "\n" and inpt != "c":
            inpt = str(raw_input("Press enter to run with default options, or \'c\' to run with custom options\n>>> "))

        if inpt == "c":
            return True

        return False

    def get_pos_int(self, prompt):
        """ Prompt the user until a positive integer is given """

        inpt = ""

        while not inpt.isdigit() or int(inpt) < 0:
            inpt = str(raw_input("Enter a number of " + prompt + " to collect >>> "))

        return int(inpt)

    def get_y_n(self, prompt):
        """ Prompt the user until a yes or no is read """

        inpt = ""

        while inpt != "y" and inpt != "n":
            inpt = str(raw_input(prompt + " [y/n] >>> "))

        if inpt == "n":
            return False

        return True

def main():
    """ Main driver for the Reddit bot """

    driver = Driver()
    bot = Bot('193bot')

    bot.get_subreddits()
    bot.get_posts(driver.post_count)
    bot.get_users(driver.user_count, driver.comment_count)

    if driver.create_output:
        bot.create_subreddit_output()
        bot.create_user_output()

    if driver.analyze:
        bot.analyze()

if __name__ == '__main__':
    main()