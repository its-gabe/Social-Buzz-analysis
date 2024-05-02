import pandas as pd
import matplotlib.pyplot as plt
from data_analysis import ranks, top5, category_mean_scores

df_company = pd.read_csv(f"data\Task_3_Final_Content_Data_set.csv")
df_original = pd.read_csv(f"data\Merged_data.csv")

df = df_original.copy()

# # TOP 5 CATEGORIES
# plt.figure(figsize=(8, 6))
# top5.plot(kind='bar')
# plt.title('Top 5 most popular categories on the website')
# plt.xlabel('Categories')
# plt.ylabel('Score')
# plt.xticks(rotation=25)
# plt.show()


ranks_plot = df.groupby(['Category'])['Score'].sum().sort_values(ascending=False)

# # HIGHEST SCORES OVERALL
# plt.figure(figsize=(10, 6))
# ranks_plot.plot(kind='bar')
# plt.xlabel('Category')
# plt.ylabel('Score')
# plt.title("Category's score")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

reaction_total = df['Category'].value_counts().sort_values(ascending=False)

# # HIGHEST AMOUNT OF POSTS
# plt.figure(figsize=(10, 6))
# reaction_total.plot(kind='bar')
# plt.xlabel('Category')
# plt.ylabel('Amount of posts')
# plt.title("Category's Total post")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()


df_company['Datetime'] = pd.to_datetime(df_company['Datetime'])
df_company['Month'] = df_company['Datetime'].dt.strftime('%B')

order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
reactions_by_month = df_company['Month'].value_counts().reindex(order)

# # AMOUNT OF POSTS ON EACH MONTH
# plt.figure(figsize=(9, 7))
# reactions_by_month.plot()
# plt.xlabel('Months')
# plt.title('Which month got the most engagement')
# plt.ylabel('Number of reactions')
# plt.xticks(range(len(reactions_by_month)), reactions_by_month.index, rotation=45)
# plt.show()

# # MEAN SCORE OF EACH CATEGORY
# plt.figure(figsize=(10, 7))
# category_mean_scores.plot(kind='bar')
# plt.title("Mean reaction's score on categories")
# plt.xlabel('Category')
# plt.ylabel('Mean score')
# plt.xticks(rotation=40)
# plt.tight_layout()
# plt.show()