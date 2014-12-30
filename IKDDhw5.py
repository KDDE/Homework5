import pandas as pd
import numpy as np
import csv as csv
import re
from sklearn.ensemble import RandomForestClassifier

predictions_file = open("result.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])

survivors_df = pd.read_csv('./csv/sur.csv', header = 0)
test_df = pd.read_csv('./csv/test.csv', header=0)

survivors = {}
survivors_name = []
predictions = {}

for passenger_index, passenger in survivors_df.iterrows():
    survivors_name.append(passenger['Name'])
    survivors[passenger['Name']] = passenger['Class']
for passenger_index, passenger in test_df.iterrows():
    f = 0
    name = re.sub(r',.*$', '', passenger['Name'])
    for s in survivors_name:
        if name.lower() in s.lower() and int(survivors[s]) is int(passenger['Pclass']):
            predictions[passenger['PassengerId']] = 1
            f = 1
        if f == 1:
            break
    if f != 1:
        predictions[passenger['PassengerId']] = 0

for key, value in predictions.items():
    open_file_object.writerow([key, value])

predictions_file.close()

print 'Done.'
