import pandas as pd
from fim import eclat, apriori
from tabulate import tabulate

df = pd.read_csv("plants_preprocessed.csv")
dataset = df.values.tolist()

print("================  ECLAT-Close ================ ")
itemsets = eclat(dataset,target='c',supp=2,report='s')
print(tabulate(itemsets,  headers=['Itemset', 'Support'], tablefmt='pretty'))


print("\n\n\n================  Apriori-Close ================ ")
itemsets = apriori(dataset,target='c',supp=2,report='s')
print(tabulate(itemsets,  headers=['Itemset', 'Support'], tablefmt='pretty'))
