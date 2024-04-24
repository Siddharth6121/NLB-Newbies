import codecs
import operator
import numpy as np
import csv
import random

def extractinfo():
    sentlist = list()
    dictlist = list()
    csv_file = 'product_review_data_without_duplicates.csv'
    train_file = 'train_without_duplicates.csv'
    test_file = 'test_without_duplicates.csv'
    validate_file = 'validate_without_duplicates.csv'
    with codecs.open('raw-tagged-sentences.txt', 'r', 'utf-8') as f, \
         open(train_file, 'w', newline='') as train_csvfile, \
         open(test_file, 'w', newline='') as test_csvfile, \
         open(validate_file, 'w', newline='') as validate_csvfile:
        train_writer = csv.writer(train_csvfile)
        test_writer = csv.writer(test_csvfile)
        validate_writer = csv.writer(validate_csvfile)
        for line in f: 
            tmp = line.rstrip().split('\t')
            column1 = tmp[0].rstrip()
            column2 = eval(tmp[-2].rstrip())
            # if column2['PRED'] and column2['PROD1'] and column2['ASP'] and column2['PROD2']:
            if column2['ASP']:
                rand_val = random.random()
                if rand_val <= 0.8:  # 80% to train set
                    train_writer.writerow([column1, column2])
                elif rand_val <= 0.9:  # 10% to test set
                    test_writer.writerow([column1, column2])
                else:  # 10% to validate set
                    validate_writer.writerow([column1, column2])
            # If you still want to populate sentlist and dictlist, uncomment the following lines
            # sentlist.append(column1)
            # dictlist.append(column2)
    return sentlist, dictlist

def findclasscount(dictlist):
    pred_count = 0
    prod1_count = 0
    asp_count = 0
    prod2_count = 0
    for entry in dictlist:
        if entry['ASP']:
            asp_count += 1
            if entry['PRED']:
                pred_count += 1
            if entry['PROD1']:
                prod1_count += 1
            if entry['PROD2']:
                prod2_count += 1

    print("Counts:")
    print("PRED:", pred_count)
    print("PROD1:", prod1_count)
    print("ASP:", asp_count)
    print("PROD2:", prod2_count)
    return

def main():
    sentlist, dictlist = extractinfo()
    # print('SENTENCE LIST',len(sentlist))
    # print('CLASSES LIST',len(dictlist))
    # findclasscount(dictlist)
    
if __name__ == '__main__':
	main()
