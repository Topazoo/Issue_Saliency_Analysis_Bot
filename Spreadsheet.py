#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu

    Description: A class to make interacting with spreadsheets via the openpyxl library easier

    Version: Python 2.7
    Requirements: openpyxl """

from openpyxl import Workbook, load_workbook
import os

class Spreadsheet(object):
    """ Class to simplify operating on Excel sheets """

    def __init__(self, filename, load=True):
        """ Params:
            @filename - The name of the excel file including the extension
            @load - Load the file if true, create it if false """

        self.filename = filename

        # If load is False, recreate excel file on every run
        # Else load the file
        if load is True:
            self.file = load_workbook(filename=filename)
        else:
            if os.path.isfile(filename):
                os.remove(filename)

            self.file = Workbook()
            self.save()

        self.sheet = self.file.active

    def save(self):
        """ Save the file """

        self.file.save(filename=self.filename)

    def write(self, content, cell):
        """ Write to a cell
            Params:
            @content - The content to write
            @cell - The cell to write to """

        self.sheet[cell] = content
        self.save()
