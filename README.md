# Social-Buzz-analysis
 project provided by accenture as a real experience working as data analyst

# Data Analysis README

This repository contains Python scripts for analyzing data related to content and reactions from a website. The data is divided into three main CSV files: `Content.csv`, `Reactions.csv`, and `ReactionTypes.csv`. The analysis is aimed at finding the top 5 categories based on popularity and other insights.

## 1. data_preparation.py

This script performs the initial data preprocessing steps:

- Loads the original data from the CSV files.
- Identifies missing values and removes them if necessary.
- Selects relevant columns for analysis.
- Merges the data frames based on content ID and reaction type.
- Cleans the `Category` column by removing quotation marks and converting all categories to lowercase.
- Calculates the sum and mean of scores for each category.
- Outputs the top 5 categories based on popularity and mean scores.

## 2. data_analysis.py

This script visualizes the analyzed data using matplotlib:

- Loads the final merged data and additional company-related data.
- Plots graphs to visualize insights:
  - Top 5 categories based on score.
  - Total score for each category, ordered by highest score.
  - Total number of posts for each category.
  - Engagement over months by plotting the number of posts in each month.
  - Mean score of each category.

## 3. README.md

This README file provides an overview of the scripts and their functionalities.

## Instructions for Use

1. Ensure that all required CSV files (`Content.csv`, `Reactions.csv`, `ReactionTypes.csv`, `Task_3_Final_Content_Data_set.csv`, and `Merged_data.csv`) are in the `data` directory.
2. Run the `data_preparation.py` script to preprocess the data and obtain insights about the top 5 categories based on popularity.
3. Run the `data_analysis.py` script to visualize the analyzed data using matplotlib.

Feel free to explore and modify the scripts as needed for your analysis.

