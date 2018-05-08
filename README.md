# Subreddit Analysis Tool
### Author: Peter Swanson
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 2.7](https://img.shields.io/badge/Python-2.7-brightgreen.svg)](https://www.python.org/downloads/release/python-2714/)
[![openpyxl](https://img.shields.io/badge/openpyxl-2.5.3-brightgreen.svg)](https://pypi.org/project/openpyxl/)
[![praw](https://img.shields.io/badge/praw-5.4.0-brightgreen.svg)](https://pypi.org/project/praw/)


## Background
Every subreddit on Reddit can be viewed as its own  online community. Each has its own rules, moderators and regular posters.
As a result, users in each employ different methods of communication to articulate a diverse array 
of political views. 

<b>This script is designed help research if/how communication styles vary
across political subreddits.</b>

This program collects information about subreddits listed in an Excel
spreadsheet, as well as information about the users of those subreddits.
This information is then written to two spreadsheets for easy viewing.

Note: Spreadsheet.py is a particularly useful tool
for writing lists of data to spreadsheet rows or columns on its own.


## Functionality
### Quick Use:
- If your input file is all set, running <b>driver.py</b> will walk you through a series of prompts. You can choose how 
 many posts, users, and comments to collect, whether to write them to a spreadsheet, and whether to analyze collected
 data.
 
 ```
 $ ./driver.py
 Press enter to run with default options, or 'c' to run with custom options
>>> c
Create output [y/n] >>> n
Analyze data [y/n] >>> n
Enter a number of posts to analyze >>> 2
Enter a number of users to analyze >>> 2
Enter a number of comments to analyze >>> 2
Running with custom options. Please wait...
 ```

### Set Up:
- Create a <b>subreddits.xlsx</b> spreadsheet containing two columns the headers:
    1. Subreddit - The name of the subreddit (e.g. r/all)
    2. Ideology - The assumed ideology of the subreddit's users
- Place the spreadsheet file in the <b>input</b> folder
- Register for <b>OAuth2</b> and create a <b>praw.ini</b> file (see requirements)

### Collecting Information:
- Open <b>Python 2.7</b> from the folder containing the <b>input</b> folder and instantiate a <b>Bot</b> object using 
the name you gave your bot when setting up PRAW
``` 
    >>> from POL193_RedditBot import Bot
    
    # bot_name - A string containing the bot's name
    >>> bot = Bot(bot_name='193bot') 
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
- Information can be written to an Excel spreadsheets in <b>output/subreddit_results.xlsx</b> and <b>output/user_results.xlsx</b> using the respective methods
```
    >>> bot.create_subreddit_output()
    Success! Data written to output/subreddit_results.xlsx
    >>> bot.create_user_output()
    Success! Data written to output/user_results.xlsx
```
- The first spreadsheet contains information about the top posts and posters in each subreddit.
- The second spreadsheet contains information about the top posters in each subreddit and their most recent comments.



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
   # Instantiate a Subreddit object given an optional name and ideology
    >>> subreddit = Subreddit(name=None, ideology=None)
    
   # Instantiate a Post object given a post
    >>> post = Post(post)
    
   # Instantiate a User object given an optional namme
    >>> user = User(name=None)
    
   # Instantiate a Comment object given a PRAW Comment
   >>> comment = Comment(comment=PRAW.Comment)
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
    
    # Store a list of the top x users and y most recent comments for each subreddit
    >>> bot.get_users(user_count=10, comment_count=10)
    >>> print bot.subreddits[0].top_posters[0]
    'Name: YElluminaty'
    >>> print bot.subreddits[0].top_posters[0].sub_comments[0]
    'Lol'
    
   # Create a spreadsheet with info about each subreddit, post and user
   >>> bot.create_subreddit_output() 
   Success! Data written to output/subreddit_results.xlsx
   
   # Create a spreadsheet with info about each user and their most recent posts
   >>> bot.create_user_output()
   Success! Data written to output/user_results.xlsx 
```        

#### Testing.py
###### Unit testing for all classes

## Requirements:
- Python 2.7 - https://www.python.org/downloads/release/python-2714/
- openpyxl - https://pypi.org/project/openpyxl/
- PRAW - https://pypi.org/project/praw/
    - Reddit OAuth2 - https://github.com/reddit-archive/reddit/wiki/OAuth2
    - A praw.ini file with your OAuth2 details - http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
    
## TODO:
- Most used words: https://pypi.org/project/redditanalysis/1.0.5/
- Word clouds: https://github.com/paul-nechifor/reddit-cloud
- Extract text from images: https://github.com/PiJoules/Text-from-Memes
- Phrase analysis: http://textblob.readthedocs.io/en/dev/