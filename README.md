Datasets used:
1. Product Reviews - https://zenodo.org/records/1415481#.W5pjkBwScnQ - This dataset has electronic product reviews with SRL labels - "PROD","PRED" and "ASP". We have used this dataset to train our LSTM model for SRL.
2. Amazon Reviews - sourced from https://github.com/jlopez873/Sentiment_Analysis_Using_Neural_Networks/tree/main?tab=readme-ov-file - This dataset contains reviews from Amazon
   and uses ratings given for the products as labels (0-5). We train our Sentiment Analysis model on this dataset. 

makedata.py - filtering product reviews dataset by retaining records with the ASPECT label marked. 

LSTM-SRL.ipynb - This code is used to train an LSTM model for SRL and compute predictions for some sample test data. The SRL labels being used are "PROD","PRED" and "ASP". 
The dataset used for training and evaluating the SRL model is Product Reviews (https://zenodo.org/records/1415481#.W5pjkBwScnQ).

generate_labels.ipynb - This code is used to compute SRL labels on the Amazon Reviews Dataset. The SRL labels generated are stored in review_with_srl.csv file.

LabelingProductReviews.ipynb - This code is used to compute sentiment labels on Product Reviews Dataset. 

SentimentAnalysisCode.ipynb - This code is used to get the benchmarking performance of LSTM for Sentiment Analysis (without SRL labels). This model is trained on Amazon Reviews Dataset.
Labels for Sentiment Analysis - Negative,Neutral and Positive. We are referring 
https://github.com/jlopez873/Sentiment_Analysis_Using_Neural_Networks/blob/main/Sentiment%20Analysis%20Using%20Neural%20Networks.ipynb for the benchmarking model. 

Under Progress:
We are currently working on using the SRL labels as features for the LSTM model for Sentiment Analysis.



