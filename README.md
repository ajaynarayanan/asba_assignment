ASBA Assignment on plants dataset
==========================================

List of files
-------------
1. preprocess.py
2. plants.csv
3. plants_preprocessed.csv
4. Frequent_Itemset_Mining.py 
5. Maximum_Frequent_Itemset_Mining.py
6. Closed_frequent_itemset_mining.py
7. Assigment.ipynb
4. requirements.txt
5. README(this file)

The dataset is a copy of the “US States Plants dataset for Connecticut" 
from `Plants Databse <https://plants.sc.egov.usda.gov/java/stateDownload?statefips=US09>`

Usage
-----
To view the assignment, use the Jupter notebook file, "Assignment.ipynb"

To preprocess the dataset provided and save it to "plants_preprocessed.csv"

    python3 preprocess.py 

To testdrive algorithms on the preprocesssed dataset for    

    1) Frequent Itemsets Mining

        python3 Frequent_Itemset_Mining.py 
   
    2) Maximum Frequent Itemsets Mining

        python3 Maximum_Frequent_Itemset_Mining.py

    3) Closed Frequent Itemsets Mining

        python3 Closed_frequent_itemset_mining.py

Requirements
-----
The requirements.txt file lists all Python libraries that this project depends on, and they can be installed using:

    pip3 install -r requirements.txt
