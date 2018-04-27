# Subreddit Analysis Tool
### Author: Peter Swanson

## Background

## Functionality
### Set Up:
- Create a <b>subreddits.xlsx</b> spreadsheet containing two columns the headers:
    1. Subreddit - The name of the subreddit (e.g. r/all)
    2. Ideology - The assumed ideology of the subreddit's users
- Place the spreadsheet file in the <b>input</b> folder
- Register for <b>OAuth2</b> and create a <b>praw.ini</b> file (see requirements)

### Collecting Information:
- Open <b>Python 2.7</b> from the folder containing the <b>input</b> folder and instantiate a <b>Bot</b> object
``` 
    >>> from POL193_RedditBot import Bot
    
    >>> bot = Bot() 
```
- Use the <b>Bot.get_subreddits()</b> and <b>Bot.get_posts()</b> methods to collect subreddit and post information respectively 
``` 
    >>> bot.get_subreddits()
    
    >>> bot.get_posts()
```
- This data is stored in the <b>Bot.subreddits</b> and <b>Bot.subreddits[index].top_posts</b> lists as Subreddit and Post
 objects respectively. 
 ``` 
    >>> print(bot.subreddits)
    [r/socialism, r/Libertarian, r/The_Donald, r/politics]
    
    >>> print bot.subreddits[0].top_posts[0]
    Title: Yup
     Poster: TheRandomSnake
     Score: 23893
     Comments: 307
     Type: Image
     Date: 2017-10-09 17:42:47
     Link: /r/socialism/comments/75ar86/yup/
```

### Recording Information:
- Information can be written to an Excel spreadsheet in <b>output/results.xlsx</b> using the <b>Bot.create_output()</b> method
```
    >>> bot.create_output()
    Success! Data written to output/results.xlsx
```

## Files
#### Spreadsheet.py
###### Simplifies reading and writing to Excel files
``` 
   # Instantiate object given a filename, loads file if load=true
    >>> sheet = Spreadsheet(filename, load=True)
    
    # Write content to a cell
    >>> sheet.write(content, cell) 
    
    # Read and store a column in a dict, header as dict key if header=true 
    >>> column = sheet.read_column(col, header=True, start_row=1)
    
    # Read and store a row in a dict, row number as dict key 
    >>> column = sheet.read_column(col, header=True, start_row=1)
    
    # Write a list of content to a column, one item per cell
    >>> column = sheet.write_column(col, content, start_row=1)
    
    # Write a list of content to a row, one item per cell
    >>> row = sheet.write_row(row, content, start_col=1)
        
    # Save the sheet
    >>> sheet.save()
```

#### Reddit.py
###### Contains classes representing Reddit objects
``` 
   # Instantiate Subreddit object given an optional name and ideology
    >>> subreddit = Subreddit(name=None, ideology=None)
    
   # Instantiate Post object given a post
    >>> post = Post(post)
    
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
    
   # Store a list of x top posts from a time range for each subreddit
   >>> bot.get_posts(limit=10, range='year')
   >>> print bot.subreddits[0].top_posts[0]
   Title: Yup
    Poster: TheRandomSnake
    Score: 23893
    Comments: 307
    Type: Image
    Date: 2017-10-09 17:42:47
    Link: /r/socialism/comments/75ar86/yup/
    
   # Create a spreadsheet with info about each subreddit, post and user
   >>> bot.create_output() 
   Success! Data written to output/results.xlsx
```        

#### Testing.py
###### Unit testing for all classes

## Requirements:
- Python 2.7 - https://www.python.org/downloads/release/python-2714/
- openpyxl - https://pypi.org/project/openpyxl/
- praw - https://pypi.org/project/praw/
    - Reddit OAuth2 - https://github.com/reddit-archive/reddit/wiki/OAuth2
    - A praw.ini file with your OAuth2 details - http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html