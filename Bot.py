#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: A class to contain, organize, and analyze Reddit data

    Version: Python 2.7
    Requirements: Spreadsheet.py and openpyxl """

from Spreadsheet import Spreadsheet

class Bot(object):
    """ Class to contain highest-order program operations """

    def __init__(self):
        # Open spreadsheets for inputs and results
        self.input_sheet = Spreadsheet("subreddits.xlsx")
        self.output_file = Spreadsheet("results.xlsx", False)

        # Create a list of subreddits
        self.subreddits = []

    def get_subreddits(self):
        """ Get info from the spreadsheet """

        # Get subreddit names
        subreddits_column = self.input_sheet.read_column(0)

        # Get subreddit ideologies
        ideology_column = self.input_sheet.read_column(1)

        # Zip and store combined information
        self.subreddits = zip(subreddits_column.values()[0], ideology_column.values()[0])



