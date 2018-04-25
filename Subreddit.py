#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: A class to contain and organize subreddit data for a particular subreddit

    Version: Python 2.7 """

class Subreddit(object):
    """ Class to hold subreddit information """

    def __init__(self, row):
        self.name = row