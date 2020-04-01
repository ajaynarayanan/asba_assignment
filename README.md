ASBA Assignment on plants dataset
==========================================

List of files
-------------
1. preprocess.py
2. plants.csv
3. plant.csv
4. README(this file)

The dataset is a copy of the “US States Plants dataset for Connecticut" 
from `Plants Databse <https://plants.sc.egov.usda.gov/java/stateDownload?statefips=US09>`_

Usage
-----
To preprocess the dataset provided and save it to "plant.csv"

    python3 preprocess.py 

To run aprori algorithm to the preprocesssed dataset

    cd Apriori
    python apriori.py -f ../plant.csv 

