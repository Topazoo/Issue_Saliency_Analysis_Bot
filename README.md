# Subreddit Analysis Tool
### Author: Peter Swanson

## Background:

## Functionality:

## Files
#### Spreadsheet.py
###### Simplifies reading and writing to excel files
``` 
   # Instantiate object given a filename, loads file if load=true
    >>> sheet = Spreadsheet(filename, load=True)
    
    # Write content to a cell
    >>> sheet.write(content, cell) 
    
    # Read and store a column in a dict, header as dict key if header=true 
    >>> column = sheet.read_column(col, header=True)
    
    >>> print(column)
    {'header': [row1, row2, row3...]}
    
    # Save the sheet
    >>> sheet.save()
```

#### Reddit.py
###### Contains classes representing Reddit objects
``` 
   # Instantiate Subreddit object given an optional name and ideology
    >>> subreddit = Subreddit(name=None, ideology=None)
    
   # Instantiate Post object given an optional title and poster
    >>> post = Post(title=None, poster=None)
    
   # Instantiate User object given an optional namme
    >>> user = User(name=None)
```        

#### Bot.py
###### Contains a class to analyze subreddits and their users
``` 
   # Instantiate Bot object reading inputs from subreddits.xlsx
    >>> bot = Bot()
    
   # Store a list of Subreddits from the input sheet
    >>> bot.get_subreddits()
    >>> print(bot.subreddits)
    [r/socialism, r/Libertarian, r/The_Donald, r/politics]
```        

#### Testing.py
###### Unit testing for all classes

## Requirements:
- Python 2.7
- Openpyxl