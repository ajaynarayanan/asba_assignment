import os, sys, os.path as osp
# Import functions for Apriori and fp-growth 
this_path = osp.split(osp.abspath(__file__))[0]
apriori_path = osp.join(this_path, "Apriori/")
fp_growth_path = osp.join(this_path, "python-fp-growth/")
sys.path += [apriori_path, fp_growth_path]
from apriori import *
from fp_growth import *

print("======== Frequent Itemset Mining ==========")

print("\n\n========Apriori==========")
file_name = "./plants_preprocessed.csv"
inFile = dataFromFile(file_name) 
minSupport = 0.03
minConfidence = 0.03
items, rules = runApriori(inFile, minSupport, minConfidence)
printResults(items, rules)

print("\n\n======== FP-growth itemsets ==========")
numeric = False
minsup = 200
runFP_growth(file_name, minsup, numeric)