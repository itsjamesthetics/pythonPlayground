'''
    Developed by: James Ald Teves
    BS Computer Science

    Instructor: Dr. Chuchi S. Montenegro
    Description: A simulation on how the Apriori algorithm works with a data set 
'''

import os
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Reading data files
def list_files_in_directory(directory, target_files):
    for dirname, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename in target_files:
                print(os.path.join(dirname, filename))

list_files_in_directory('.', ['Groceries data.csv', 'Basket.csv'])

# Loading datasets
groceries_df = pd.read_csv("Groceries data.csv")

# Display unique values
print(f"\n\t Unique Values in Member ID: {len(groceries_df['Member_number'].unique())}")
print(f"\n\t Unique Values in Item Columns: {len(groceries_df['itemDescription'].unique())}")

# Frequent Items Analysis
frequent_items = groceries_df['itemDescription'].value_counts()
print("\n\t Top 10 Frequent Items: ")
print(frequent_items.head(10))

# Preparing data for Apriori Algorithm
items_by_user = [list(groceries_df.loc[groceries_df['Member_number'] == id, 'itemDescription']) 
for id in groceries_df['Member_number'].unique()]

transaction_encoder = TransactionEncoder()
transaction_encoder.fit(items_by_user)
item_matrix = pd.DataFrame(transaction_encoder.transform(items_by_user), columns=transaction_encoder.columns_)

# Applying Apriori Algorithm
frequent_itemsets = apriori(item_matrix, min_support=0.01, use_colnames=True, max_len=2)
print("\n\t Frequent Itemsets: ")
print(frequent_itemsets)

# Generating Association Rules
association_rules_df = association_rules(frequent_itemsets, metric="confidence", min_threshold=0)
print("\n\t Association Rules: ")
print(association_rules_df)

# Add a column for Zhang's score
print("\n\t Zhang's Score: ")
def calculate_zhangs_score(rules_df):
    rule_support = rules_df['support']
    rule_ante = rules_df['antecedent support']
    rule_conseq = rules_df['consequent support']
    numerator = rule_support - (rule_ante * rule_conseq)
    denominator = np.maximum(rule_support * (1 - rule_ante), rule_ante * (rule_conseq - rule_support))
    return numerator / denominator

zhangs_score = calculate_zhangs_score(association_rules_df)
association_rules_df['zhang'] = zhangs_score
print(association_rules_df.head())