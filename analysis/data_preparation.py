# Looking for missing values, changing data type and removing columns if necessary
# MAIN GOAL --> FIND THE TOP 5 CATEGORIES ON POPULARITY
import pandas as pd

## load original data

content_temp = pd.read_csv('data\Content.csv')
reaction_temp = pd.read_csv('data\Reactions.csv')
reactiontype_temp = pd.read_csv('data\ReactionTypes.csv')

### verifying the data ###



## Null values
#------------------------------

# print(content_temp.isna().sum())
### results:
# content has 199 null in URL
# reaction has 3019 null in User ID and 980 in Type
# reactiontype has none

#------------------------------




## Columns
#------------------------------

# print(content_temp.columns)
### results:
# Content ID, User ID, Type, Category, URL --> content
# Content ID, User ID, Type, Datetime --> reaction
# Type, Sentiment, Score --> reactiontype

#------------------------------



## Insights
#------------------------------

# I wont need the column datetime in reactiontype to find the most popular categories
# user ID also look useless since I don't need to know anything about the person but his reactions to contents
# URL is just the link for the post so theres no use for it
# Content ID is usefull since we have way more reactions than anything else so we need to track which content got more visibility
# type, sentiment, category and score seem to be most important for the main goal

#------------------------------



## What to do
#------------------------------

# drop columns datetime(reactiontype), user ID(content and reaction), URL(content) [x]
# remove the null lines in reaction [x]

#------------------------------

content_temp.drop(['Unnamed: 0', 'User ID', 'URL'], axis=1, inplace=True)
reaction_temp.drop(['Unnamed: 0', 'User ID', 'Datetime'], axis=1, inplace=True)
reactiontype_temp.drop(['Unnamed: 0'], axis=1, inplace=True)

reaction_temp.dropna(axis=0, inplace=True)

