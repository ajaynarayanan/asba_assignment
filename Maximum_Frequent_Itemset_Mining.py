import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpmax
from mlxtend.frequent_patterns import association_rules
from fim import eclat
from tabulate import tabulate

df = pd.read_csv("plants_preprocessed.csv")
print("================ FP-Max ==================")
dataset = df.values.tolist()
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
itemsets = fpmax(df, min_support=0.001, use_colnames=True,max_len = 10)
print(itemsets)

print("\n\n RULES based on FP growth : \n\n")
rules = association_rules(itemsets, min_threshold=0.0001,support_only=True)
print(rules[['antecedents', 'consequents', 'support']])

print("================ ECLAT-Max ================ ")
itemsets = eclat(dataset,target='m',supp=2,report='s')
print(tabulate(itemsets,  headers=['Itemset', 'Support'], tablefmt='pretty'))