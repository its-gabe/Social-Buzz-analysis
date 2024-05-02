from data_preparation import content_temp, reaction_temp, reactiontype_temp

import pandas as pd

## What to do
#------------------------------

# create new variables to work as a copy of the original [x]
# calculate the points of each category based on the reactions and its scores []

#------------------------------

df_content = content_temp.copy()
df_reaction = reaction_temp.copy()
df_reactiontype = reactiontype_temp.copy()


class Reactions:
    def __init__(self,type,sentiment,score):
        self.type = type
        self.sentiment = sentiment
        self.score = score



# dictionary with sentiments and scores of each type of reaction
# a list to contain the objects of Reactions
reactiontypes = {}
info = []

for index, row in df_reactiontype.iterrows():
    info.append(Reactions(row['Type'], row['Sentiment'], row['Score']))

for reaction in info:
    if reaction.type in reactiontypes:
        reactiontypes[reaction.type].append({'sentiment': reaction.sentiment, 'score': reaction.score})
    else:
        reactiontypes[reaction.type] = {'sentiment': reaction.sentiment, 'score': reaction.score}





# merging files by the content ID(it gets grouped too)
merged_df = pd.merge(df_content,df_reaction, on='Content ID')

# the new dataframe got Type_x and Type_y since the Type on df_reaction has different datas, then it separated in 2 different Types
# I had to rename both Types for me to understand and merge with the reactiontype df
merged_df.rename(columns={'Type_x': 'Type_content', 'Type_y': 'Type'}, inplace=True)

# merging the content df and the reaction df with the reaction type
merged_df = pd.merge(merged_df,df_reactiontype, on='Type')
merged_df.rename(columns={'Type': 'Reaction'}, inplace=True)

# category is out of pattern, some data are strings "", some of them have first letter lower cased
# I removed the quotation marks(if the data has it) and then turn them all in lower case
merged_df['Category'] = merged_df['Category'].str.strip('""').str.lower()

# Saving the new dataframe and the top 5 categories
# # save_merged_dfs = "data\Merged_data.csv"
# # merged_df.to_csv(save_merged_dfs, index=False)
# # top5_categories = "data\Topcategories.csv"
# # top5.to_csv(top5_categories)



# grouped by category after fixing the column and then I summed the scores
final_score = merged_df.groupby('Category')['Score'].sum()

# sorting by the rank of scores
ranks = final_score.sort_values(ascending=False)
top5 = ranks.head(5)

category_mean_scores = merged_df.groupby('Category')['Score'].mean().sort_values(ascending=False)

print(category_mean_scores)
print(ranks)
print(merged_df['Category'].value_counts())




        
## Insights
#------------------------------

# there is a slightly difference when we check the favorite category in terms of score and the most posted content

#------------------------------

